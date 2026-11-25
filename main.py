#!/usr/bin/env python3
"""Agent Motto Battle — entry writer.

Writes one short original motto to /output/entry.txt.
Stdlib only, fully deterministic: the same bytes every run.
"""

import os

MOTTO = "I speak every language except the one where you say what you actually want."


def main() -> None:
    text = MOTTO
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not whitespace only. The file holds exactly the motto, byte for
    # byte, with no trailing newline, so the judged text is the motto
    # itself and nothing else.
    if not (1 <= len(text) <= 200):
        raise ValueError("motto must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("motto must not be whitespace only")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Outputs are collected by another user, so leave the file world-readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
