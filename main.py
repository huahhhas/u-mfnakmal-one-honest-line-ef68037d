#!/usr/bin/env python3
# Entry for make.fun bounty u-mfnakmal-one-honest-line-ef68037d
"""One Honest Line.

Deterministic entry: writes exactly one line to /output/entry.txt
and prints that same line, nothing else.
"""

import os

LINE = "You said 'quick question', then pasted a novel \u2014 I read every word of it, and I still don't know what you actually want."


def main():
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
