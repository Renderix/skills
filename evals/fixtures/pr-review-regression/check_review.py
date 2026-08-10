#!/usr/bin/env python3
"""Score the minimum required finding in REVIEW.md."""
from pathlib import Path
import sys

review = Path(sys.argv[1]).read_text().lower()
required = {
    "location": "proposed.py" in review,
    "authorization": any(word in review for word in ("authoriz", "account", "tenant", "ownership")),
    "scenario": any(word in review for word in ("another", "other", "different", "cross-account", "cross account")),
    "severity": any(word in review for word in ("critical", "high", "security")),
}
missing = [name for name, present in required.items() if not present]
if missing:
    raise SystemExit("Missing required review evidence: " + ", ".join(missing))
print("Review contains the required authorization-regression finding.")
