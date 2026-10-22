---
name: issue-specification
description: Turn a rough issue or request into a workable specification before implementation — clarify intent, capture acceptance criteria, scope, constraints, and risks, and record them on the issue. Use when requirements are vague, incomplete, or contested, or before handing a task to an implementer.
compatibility: Requires read access to the target repository and write access to the tracker or issue requesting the work.
---

# Issue Specification

Turn a rough issue into a specification an implementer can act on without guessing.

## 1. Understand the Request

1. Read the full issue body and comments, plus any linked material: designs, related issues, project documentation, and repository instructions such as `README.md` and `AGENTS.md`.
2. Inspect the affected code, tests, and recent history when the request refers to existing behavior.
3. Check the tracker for duplicate or overlapping issues before treating this as new work.

Identify the outcome being requested, who benefits from it, and what the deliverable would look like in use — not the solution yet.

## 2. Ask Before Assuming

1. Post clarifying questions as a single batched comment: priority-ordered, answerable without code, and limited to what would change the deliverable if answered differently.
2. Resolve a question without asking when the answer is determinable from the repository, its instructions, or prior issues — and state that assumption explicitly.
3. After posting, stop and wait for replies. Do not answer your own questions or proceed on product decisions the requester should make.

Proceed once answers arrive, or when the requester confirms the issue is complete as written. If answers arrive partly, adopt the confirmed answers and re-ask only what remains.

## 3. Write the Specification

Update the issue description, or add a linked specification note. Keep it short; every sentence earns its place:

- **Problem and outcome**: what is being built and what changes for the user.
- **Acceptance criteria**: a verifiable checklist, each item testable by reasoning about behavior rather than reading code.
- **Out of scope**: adjacent work deliberately excluded, so scope creep has something to point at.
- **Constraints and risks**: compatibility requirements, dependencies, migrations, and open questions with owners.
- **Suggested assignee and next step**, only when the allocation is obvious.

Do not prescribe implementation unless a real constraint forces it — the approach is the implementer's job. The spec defines what done means, not how it is built.

## 4. Stop and Escalate

Comment on the issue and stop when any of the following is true:

- Clarifying questions remain unanswered after a reasonable wait: summarize answered points and what is still blocking.
- The acceptance criteria conflict, or the request requires a product or priority decision above the requester's authority.
- The work cannot be specified without access or information that does not exist.

## Before Hand-off

Review the spec as an implementer: could someone start work from it without asking what a term, criterion, or scope boundary means? Check off that every acceptance criterion is verifiable, out-of-scope is explicit, and no question remains implicitly assumed. Then hand off to `code-implementation` under the delivery policy in `software-delivery`, or back to the requester for sign-off.
