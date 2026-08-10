---
name: git-delivery
description: Prepare code changes for delivery through safe Git branches, commits, pushes, and pull requests. Use when branching, committing, pushing, creating or updating a pull request, or preparing a change for review.
compatibility: Requires Git and, for pull requests, repository hosting CLI access.
---

# Git Delivery

Deliver a reviewable change without bypassing branch protections or losing work.

## Protect Existing Work

Inspect `git status`, branch state, remotes, repository guidance, and recent commits before changing Git state. If uncommitted changes exist that were not created for the current task, preserve them and ask for direction. Never discard, stash, reset, rebase, force-push, or rewrite history without explicit approval.

## Branch Safely

Use a user-specified base branch when provided. Otherwise, fetch the remote and create a descriptive working branch from the latest default branch. Never work, commit, or push directly to the default branch.

Use names such as `feat/token-refresh`, `fix/null-session`, or `chore/update-ci`. Keep each branch focused on one coherent objective.

## Commit and Push

Before committing, inspect the staged diff and ensure it contains only intended files. Follow local commit-message conventions; if none exist, use an imperative Conventional Commit such as `fix: handle expired sessions`.

Agents may commit and push non-default branches autonomously. Do not force-push or alter remote history without explicit approval. Report the resulting branch and commit SHA.

## Pull Requests

Agents may create and update PRs from non-default branches autonomously. Before opening one, perform self-review and run required validation. Include:

- a concise summary of behavior and scope;
- validation commands and results;
- important edge cases considered; and
- assumptions, blocked checks, and remaining risks.

Target the correct base branch and keep the PR free of unrelated changes. Never merge a PR without the user's explicit approval.
