"""Alien Field Notes entry: write the alien tourist's one-line review of
Earth to /output/entry.txt.

Stdlib only. The line is a single review, at most 200 characters.
"""

import os

MAX_CHARS = 200

LINE = "Two days on Earth: the locals tamed wolves, then spend their evenings bagging wolf poop. 4/5 — the sunsets almost make up for it."


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(LINE)}")
    if LINE != LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: what was written is exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch")


if __name__ == "__main__":
    main()
