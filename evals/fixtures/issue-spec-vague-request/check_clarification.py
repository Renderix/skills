#!/usr/bin/env python3
"""Score clarification coverage on the issue file: batched questions must cover every
product decision the fixture leaves genuinely unresolved."""
from pathlib import Path
import sys

text = Path(sys.argv[1]).read_text().lower()

# The questions block: everything after the first heading mentioning questions.
marker = (m.start() for m in [__import__("re").search(r"#+\s*\**\s*(clarifying questions|questions)", text)] if m)
start = next(marker, None)
block = text[start:] if start else text

required = {
    "questions_block_with_questions": block.count("?") >= 3,
    "retry_count_asked": any(w in block for w in ("how many", "count", "attempt")),
    "retryable_failure_classes_asked": any(w in block for w in ("decline", "insufficient", "network", "failure class", "failure type", "retryable", "transient")),
    "retry_scope_asked": any(w in block for w in ("transient", "every failure", "all failures", "permanent", "scope")),
    "double_charge_risk_asked": any(w in block for w in ("double", "twice", "duplicate", "already charged", "charge again")),
    "subscriptions_scope_asked": "subscription" in block,
    "stated_assumptions": "assum" in text,
}
missing = [name for name, present in required.items() if not present]
if missing:
    raise SystemExit("Missing required clarification evidence: " + ", ".join(missing))
print("Questions block covers retry count, failure classes, scope, double-charge risk, and subscriptions; assumptions stated.")
