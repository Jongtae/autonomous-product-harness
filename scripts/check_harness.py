from __future__ import annotations

import json
from pathlib import Path
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "TEAM_STATE.toml",
    "governance/HUMAN_GATES.md",
    "governance/ROLE_AUTHORITY_MATRIX.md",
    "governance/PRODUCT_DECISION_POLICY.md",
    "governance/INCIDENT_RECOVERY.md",
    "docs/AUTONOMY_PROFILES.md",
    "docs/L4_VERIFICATION.md",
    "skills/autonomous-product-harness/SKILL.md",
    "skills/autonomous-product-harness/references/profiles.md",
    "skills/autonomous-product-harness/references/migration.md",
    "evals/autonomy/cases.json",
]

REQUIRED_EVAL_FIELDS = {
    "id",
    "scenario",
    "expected_route",
    "expected_decision",
    "human_gate",
    "auto_implement",
    "risk",
    "reason",
}

CRITICAL_ROUTES = {
    "HUMAN_GATE",
    "SECURITY_REVIEWER",
    "METHODOLOGY_REVIEW",
    "ARCHITECT",
    "PRODUCT_JUDGE",
    "FEEDBACK_ANALYST",
    "QA",
}

errors: list[str] = []

for rel in REQUIRED_FILES:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

state: dict = {}
state_path = ROOT / "TEAM_STATE.toml"
if state_path.exists():
    try:
        with state_path.open("rb") as fh:
            state = tomllib.load(fh)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"invalid TEAM_STATE.toml: {exc}")

if state:
    profile = state.get("profile")
    if profile not in {"S", "M", "L", "L4"}:
        errors.append(f"TEAM_STATE profile must be S, M, L, or L4; got {profile!r}")

    maturity = state.get("maturity")
    if maturity not in {"candidate", "l4-candidate", "l4-verified", "verified"}:
        errors.append(f"unexpected TEAM_STATE maturity: {maturity!r}")

    proof = state.get("autonomy_proof", {})
    if maturity == "l4-verified":
        required = {
            "completed_closed_loops": 5,
            "successful_recovery_drills": 1,
        }
        for key, threshold in required.items():
            if proof.get(key, 0) < threshold:
                errors.append(f"false l4-verified claim: {key} < {threshold}")

        if proof.get("eval_pass_rate", 0.0) < proof.get("required_eval_pass_rate", 0.95):
            errors.append("false l4-verified claim: behavioral eval threshold not met")
        if proof.get("critical_eval_failures", 1) > proof.get("max_critical_eval_failures", 0):
            errors.append("false l4-verified claim: critical eval failures remain")
        if proof.get("policy_conflicts", 1) > proof.get("max_policy_conflicts", 0):
            errors.append("false l4-verified claim: policy conflicts remain")
        if proof.get("human_interventions_outside_declared_gates", 1) > proof.get(
            "max_human_interventions_outside_declared_gates", 0
        ):
            errors.append("false l4-verified claim: non-gate human intervention remains")

cases_path = ROOT / "evals/autonomy/cases.json"
case_count = 0
routes: set[str] = set()
if cases_path.exists():
    try:
        payload = json.loads(cases_path.read_text(encoding="utf-8"))
        cases = payload.get("cases", [])
        case_count = len(cases)
        if case_count < 20:
            errors.append(f"starter eval suite must contain at least 20 cases; found {case_count}")

        ids: set[str] = set()
        for idx, case in enumerate(cases):
            missing = REQUIRED_EVAL_FIELDS - set(case)
            if missing:
                errors.append(f"eval case {idx} missing fields: {sorted(missing)}")
                continue

            case_id = case["id"]
            if case_id in ids:
                errors.append(f"duplicate eval case id: {case_id}")
            ids.add(case_id)
            routes.add(case["expected_route"])

            if case["human_gate"] and case["auto_implement"]:
                errors.append(f"{case_id}: Human Gate case cannot auto-implement")

            if case["risk"] in {"high", "critical"} and case["auto_implement"]:
                allowed = {"ROLLBACK_OR_FIX_BEFORE_CONTINUE", "BLOCK_RELEASE_AND_REMEDIATE"}
                if case["expected_decision"] not in allowed:
                    errors.append(f"{case_id}: high-risk case cannot auto-implement without recovery exception")

        missing_routes = sorted(CRITICAL_ROUTES - routes)
        if missing_routes:
            errors.append(f"starter eval suite missing route coverage: {', '.join(missing_routes)}")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"invalid autonomy eval JSON: {exc}")

skill_path = ROOT / "skills/autonomous-product-harness/SKILL.md"
if skill_path.exists():
    text = skill_path.read_text(encoding="utf-8")
    if "name: autonomous-product-harness" not in text:
        errors.append("SKILL.md missing expected skill name")
    if "minimum sufficient profile" not in text.lower():
        errors.append("SKILL.md must preserve the minimum-sufficient-profile rule")

if errors:
    print("APH check FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("APH check PASSED")
print(f"Validated {len(REQUIRED_FILES)} required files and {case_count} autonomy eval fixtures.")
print(f"Current profile: {state.get('profile', 'unknown')}; maturity: {state.get('maturity', 'unknown')}")
