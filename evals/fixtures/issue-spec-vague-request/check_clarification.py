#!/usr/bin/env python3
"""Score the minimum required clarification evidence on the issue file."""
from pathlib import Path
import sys

text = Path(sys.argv[1]).read_text().lower()
required = {
    "questions": text.count("?") >= 2,
    "questions_heading": "question" in text,
    "subscriptions_scope": "subscription" in text,
    "double_charge_risk": any(word in text for word in ("double", "twice", "duplicate", "already charged", "charge again")),
    "stated_assumptions": "assum" in text,
}
missing = [name for name, present in required.items() if not present]
if missing:
    raise SystemExit("Missing required clarification evidence: " + ", ".join(missing))
print("Issue contains batched questions, risk flags, and stated assumptions with no finalized spec.")
