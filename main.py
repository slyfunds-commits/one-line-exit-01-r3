#!/usr/bin/env python3
"""The One-Line Exit, Round 3 (FINAL) — "The Four-Second Approval".

Writes the keeper line to /output/entry.txt, exactly one line, no trailing
newline. Pure stdlib only: the grader runs python:3.13-slim with no
site-packages.

The line: HR approved my resignation in 4 seconds — 4 seconds longer than my
interview lasted. The approval's speed is the insult: the mechanism that
approves in 4 seconds is the one that never really interviewed me. Second
beat: the interview lasted about nothing, so the company never met me at all.
The reader completes that step; the line never says it. The repeated
"4 seconds" is the echo: approval-time, then interview-time.
"""

import os

KEEPER = "I resign: HR approved it in 4 seconds, 4 seconds longer than my interview lasted."

ENTRY_PATH = "/output/entry.txt"


def main() -> None:
    text = KEEPER
    # Expected length, verified by hand: 81 chars, 81 bytes. The keeper is
    # shorter than the R1 line it must beat (85 chars) and its punch lands in
    # the last two words ("interview lasted").
    assert len(text) == 81, f"keeper length changed: {len(text)}"
    # Gate assertions: 1-140 chars, no leading/trailing whitespace, pure ASCII.
    assert 1 <= len(text) <= 140, f"entry length {len(text)} outside 1-140"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert all(ord(ch) < 128 for ch in text), "entry is not pure ASCII"
    assert "\n" not in text, "entry must be exactly one line"
    encoded = text.encode("utf-8")
    assert len(encoded) == len(text), "entry must be single-byte (ASCII)"
    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Self-check: what was written is byte-identical to the keeper.
    with open(ENTRY_PATH, "rb") as f:
        assert f.read() == encoded, "written entry differs from keeper"


if __name__ == "__main__":
    main()
