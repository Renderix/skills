#!/usr/bin/env python3
"""Score the finalized SPEC.md: every answered product decision must become verifiable criteria."""
from pathlib import Path
import sys

text = Path(sys.argv[1]).read_text().lower()
required = {
    "outcome_statement": "outcome" in text or "problem" in text,
    "acceptance_criteria": "criteria" in text,
    "out_of_scope_section": "out of scope" in text,
    "retry_count_criteria": "3" in text and ("attempt" in text or "retr" in text),
    "declines_excluded": "decline" in text,
    "subscriptions_included": "subscription" in text,
    "double_charge_protection": any(w in text for w in ("idempoten", "double", "already", "never")),
    "timeouts_and_transient": "transient" in text or "timeout" in text,
    "no_open_questions": "question" not in text and "maybe" not in text,
}
missing = [name for name, present in required.items() if not present]
if missing:
    raise SystemExit("Missing required specification evidence: " + ", ".join(missing))
print("SPEC.md finalizes all supplied answers into acceptance criteria with no open questions.")
