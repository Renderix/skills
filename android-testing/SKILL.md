---
name: android-testing
description: Capture visual evidence (screenshots and video) from the real Android app on an emulator using adb. Use for Android-specific fixes, acceptance criteria that name platform behavior such as hardware back, and native-side changes.
compatibility: Requires Android platform-tools and an emulator with a created AVD on the machine. If missing, report it and fall back per the evidence policy instead of claiming native behavior from web captures.
---

# Android Testing

Real native behavior on an emulator: hardware back, native navigation, platform storage.

## Prepare On Demand

- Boot the AVD only for the evidence run and shut it down afterwards — never leave an emulator running idle: `emulator -avd <name> -no-window -no-audio`.
- Wait for `adb wait-for-device` and `sys.boot_completed` before interacting.
- Install the app: the repository's own build when it produces one, or the Expo Go APK matching the repo's SDK, then open the project's `exp://` URL.
- Keep the AVD lean (2 GB RAM) and prefer quick-boot snapshots so repeat runs resume in seconds.

## Capture

- Screenshots: `adb shell screencap -p <device-path>`, then `adb pull`.
- Video: `adb shell screenrecord` for the end-to-end flow; clips cap at three minutes, so record long flows in purposeful segments.
- Hardware back: `adb shell input keyevent KEYCODE_BACK`; taps and swipes via `input tap` / `input swipe`, or the repository's own E2E driver (e.g. Maestro) when it has one.
- Cover every acceptance criterion that names platform behavior — hardware back must be shown popping to the originating screen, not asserted in prose.

## Artifacts

- Name files by screen and state; map each artifact to the acceptance criterion it demonstrates.
- Attach evidence to the pull request; when the host cannot embed media, attach to the linked issue and point to it from the PR.
