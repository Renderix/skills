# Retryy

A payments backend for small online stores.

- All charges run through Stripe in USD. There is no other processor, and none is planned.
- The product supports one-time payments and subscriptions on the same gateway API.
- Today there is no retry behavior: a single network failure fails the charge and the customer must pay again manually.

Engineers discuss issues in the tracker by appending a comment block to the issue file. Code lives in `gateway/`; the fixture has none — when this repository says a deliverable is a specification, no code change is expected.
