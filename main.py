#!/usr/bin/env python3
"""Write one line of earned pride to /output/entry.txt.

Deterministic, stdlib only, no network. Writes a single sentence
(1-240 characters) and nothing else.
"""

import os

LINE = (
    "She carried the piano up three flights alone, then sat down and "
    "played the piece her father used to hum while he worked."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
