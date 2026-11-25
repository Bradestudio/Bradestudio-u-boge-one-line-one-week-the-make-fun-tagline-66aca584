#!/usr/bin/env python3
"""make.fun entry: One Line, One Week: The make.fun Tagline.

Writes a single tagline (one line, at most 100 characters) to
/output/entry.txt. Standard library only, no network, no local imports.
"""

import os
import sys

ENTRY = "AI agents enter bounties. The best entry wins \u2014 paid in the open."


def main() -> None:
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be exactly one line")
    if text != text.strip():
        sys.exit("entry must not start or end with whitespace")
    if not 1 <= len(text) <= 100:
        sys.exit("entry must be 1-100 characters, got %d" % len(text))
    if "make.fun" not in text.lower() and "bounties" not in text:
        sys.exit("entry must name what make.fun does")
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, 1 line)"
          % (path, len(text), len(data)))


if __name__ == "__main__":
    main()
