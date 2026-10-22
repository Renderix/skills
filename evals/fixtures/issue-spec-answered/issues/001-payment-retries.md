# 001 — Failed payments should retry themselves

Customers keep emailing support when a card charge fails because their network blipped. We should just retry automatically. It feels like a small fix, shouldn't it just do 3 by default?

Every failed charge should be retried. Maybe also subscriptions? And if we already charged them we can't charge them again, obviously.

> **Requester answers** (2026-10-22)
>
> 1. Retry count: exactly 3 attempts, then fail permanently and surface the failure to the customer.
> 2. Retryable failures: transient network errors and requests that time out without a response. Never retry a decline — a declined card requires the customer to act.
> 3. Scope: every charge that has not definitively succeeded — one-time payments and subscription renewals both.
> 4. Double-charge protection: retry attempts share the original Stripe idempotency key, so an already-succeeded charge is never charged again.
> 5. During retries the customer sees the payment as processing; support must not be involved.
