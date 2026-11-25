#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would put in a commit right after it broke
production at 3 AM.
"""

import os

MESSAGE = (
    "fix: reverted my 3 AM deploy \u2014 I was 99% confident, "
    "the tests were 0% passing, and prod asked me to stop helping"
)


def main() -> None:
    text = MESSAGE.strip()
    assert 1 <= len(text) <= 200, f"message is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "message must be a single line"
    assert text.strip(), "message must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
