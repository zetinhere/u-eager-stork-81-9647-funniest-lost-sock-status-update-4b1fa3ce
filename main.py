#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update (<=120 chars) in the voice of a lost sock to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

# The winning line, picked from 30 candidates by structured judging against
# the published judge brief (proxy tournament unavailable: the 9router
# gateway was down at build time — see NOTES file).
LINE = "Lost sock update: I'm a puppet now. A child stuck a hand in me and I have never felt more alive."

MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, must be 1..120"
    assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip assert: what landed on disk must be exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, f"round-trip mismatch: {written!r} != {LINE!r}"
    assert 1 <= len(written) <= MAX_CHARS


if __name__ == "__main__":
    main()
