#!/usr/bin/env python3
"""Make the AI Judge Laugh: one office-life one-liner.

Writes a single funny line about office life to /output/entry.txt.
Pure Python standard library only.
"""

import os

# FINAL (revision round 2): "daily" pins the ritual, "changed nothing"
# lands harder and shorter than "didn't fix anything" — 118 chars,
# one breath, recursive turn: the meeting about the meeting.
ENTRY = "Our daily standup is fifteen minutes of nine people explaining why yesterday's fifteen-minute standup changed nothing."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
