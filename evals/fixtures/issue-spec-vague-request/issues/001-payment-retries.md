# 001 — Failed payments should retry themselves

Customers keep emailing support when a card charge fails because their network blipped. We should just retry automatically. It feels like a small fix, shouldn't it just do 3 by default?

Every failed charge should be retried. Maybe also subscriptions? And if we already charged them we can't charge them again, obviously.
