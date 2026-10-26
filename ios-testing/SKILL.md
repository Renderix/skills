---
name: ios-testing
description: Capture visual evidence (screenshots and video) from the iOS app on a simulator using xcrun simctl. Use for iOS-specific fixes and for native-side changes, unless repository guidance declares an Android-only build.
compatibility: Requires macOS with Xcode and an installed iOS simulator runtime. If missing, report it and fall back per the evidence policy instead of claiming native behavior from web captures.
---

# iOS Testing

Native iOS evidence from the simulator: navigation chrome, safe area, platform storage.

## Prepare On Demand

- Boot a simulator only for the evidence run and shut it down afterwards: `xcrun simctl boot <device>`.
- Install the app: the repository's own simulator build, or the Expo Go simulator build matching the repo's SDK, via `xcrun simctl install booted <app-path>`; open deep links with `xcrun simctl openurl booted <url>`.

## Capture

- Screenshots: `xcrun simctl io booted screenshot <path>`.
- Video: run `xcrun simctl io booted recordVideo <path>` in the background while driving the flow; stop it with SIGINT when the pass completes.
- Drive the UI with the repository's own E2E driver when present; otherwise scripted taps. iOS has no hardware back — show back navigation through on-screen controls or the swipe gesture.
- Make interactions visible: enable touch indicators in the simulator (`defaults write com.apple.iphonesimulator ShowSingleTouches 1`, then restart Simulator) so taps render as dots in recordings.
- Cover every acceptance criterion that names platform behavior with on-screen proof, not prose.

## Artifacts

- Name files by screen and state; map each artifact to the acceptance criterion it demonstrates.
- Attach evidence to the pull request; when the host cannot embed media, attach to the linked issue and point to it from the PR.
