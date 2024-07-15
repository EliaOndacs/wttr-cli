# WTTR.IN CLI TOOL

## DESCRIPTION

The Unofficial Wttr.in cli tool build in python

## BUILD INSTRUCTION

run the build.sh with your platform as the first argument

Windows:

    win32: 32-bit Windows
    win64: 64-bit Windows
    win-arm64: 64-bit Windows on ARM (experimental)

macOS:

    macos64: 64-bit macOS (Intel)
    macos-arm64: 64-bit macOS (Apple Silicon, experimental)

Linux:

    linux32: 32-bit Linux
    linux64: 64-bit Linux
    linux-armv6l: 32-bit Linux on ARMv6 (e.g., Raspberry Pi)
    linux-armv7l: 32-bit Linux on ARMv7 (e.g., Raspberry Pi 2)
    linux-aarch64: 64-bit Linux on ARMv8 (e.g., Raspberry Pi 3)

Other:

    darwin: macOS (deprecated, use macos64 instead)
    cygwin: Cygwin (a Unix-like environment on Windows)

> Note
> any platform should be supported by pyinstaller "--platform=" flag
> please check before running

after the build is complete the executable should be in "dist/" directory

## INFO

check out wttr.in [repo](https://github.com/chubin/wttr.in)

original wttr.in author: Igor Chubin

enjoy!:upside_down_face:
