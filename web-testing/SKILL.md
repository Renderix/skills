---
name: web-testing
description: Capture visual evidence (screenshots and video) of a web build with Playwright. Use by default when an issue names no specific platform, or as the labeled fallback when emulator or simulator capture is unavailable.
compatibility: Requires the repository's web dev server and Playwright (or equivalent browser automation) tooling.
---

# Web Testing

The default visual-evidence platform: fast, headless, no device setup.

## Scope and Limits

Use for routes, layout, rendering, params, and client-side behavior. Web captures can never demonstrate platform behavior: hardware back buttons, native navigation chrome, safe-area insets, or platform storage (AsyncStorage falls back to localStorage on web). State these limits explicitly wherever the evidence is presented — never let a web capture read as proof of native behavior.

## Capture

- Start the repository's normal web build (its documented dev server, e.g. `expo start --web`).
- Drive it with the repository's existing Playwright setup; extend local scripts rather than inventing a parallel harness.
- Use a device-like viewport for mobile apps.
- Screenshot every screen and state the change touches, from a clean known state.
- Record the full end-to-end flow as video (Playwright `recordVideo` or trace) when the change spans screens; one continuous pass beats fragments.

## Artifacts

- Save under a stable, git-ignored artifacts directory; name files by screen and state (`category-detail_params.png`, `flow-end-to-end.webm`).
- Map each artifact to the acceptance criterion it demonstrates.
- Attach evidence to the pull request; when the host cannot embed media, attach to the linked issue and point to it from the PR.
