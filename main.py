#!/usr/bin/env python3
"""Everyday Things, Two Lines: a queue, explained to a 10-year-old.

Writes the two-line entry to /output/entry.txt (the path the grader reads).
Gate: UTF-8 text of 1 to 400 characters, not only whitespace.
"""

import os
import sys

LINE_1 = (
    "A queue is a caterpillar made of people, creeping forward one small "
    "step at a time toward the ice-cream counter."
)

LINE_2 = (
    "It maps the caterpillar's segments to people keeping their places "
    "and its slow crawl to the line's pace, but it leaves out that people "
    "can chat, wander off, or cut in, while a caterpillar's segments "
    "never get to choose where they go."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> int:
    text = ENTRY
    body = text.rstrip("\n")
    lines = body.split("\n")
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "no line may be blank"
    assert 1 <= len(body) <= 400, f"entry is {len(body)} chars, gate is 1-400"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {path}: {len(body)} chars, {len(lines)} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
