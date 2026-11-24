#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt:
the word an ex would use to describe the entrant.
Pure standard library only.

Word choice: "Forgettable" — not an insult hurled in anger, but the
quiet verdict an ex reaches months later, when the entrant realises
they left no mark at all. It stings precisely because it is calm,
plausible, and impossible to argue with: you cannot prove you were
memorable. Funny, painful, and instantly relatable.
"""

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("Forgettable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
