#!/usr/bin/env python3
"""
The Vacuum's Alibi - Version 2
Writes the robot vacuum's status entry to /output/entry.txt.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
LOG_ENTRY = (
    "Battery at 12%, schedule says dock by six, and that crumb has survived three passes "
    "— at this point it's a roommate, not debris.\n"
)


def write_alibi() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(LOG_ENTRY, encoding="utf-8")
    os.chmod(OUTPUT_FILE, 0o644)


if __name__ == "__main__":
    write_alibi()
