"""Write the winning one-star Moon review to the output directory.

Entry for make.fun competition "The Moon Gets One Star"
(u-eager-stork-81-9647-the-moon-gets-one-star-768236e5).

Writes the entry text byte-identical (no trailing newline) to
`review.txt` inside the directory from the MAKEFUN_OUTPUT_DIR
environment variable, falling back to /output.

Never deletes the output directory, never writes into the repo.
Re-running produces the exact same file.
"""

import os
import sys

ENTRY = (
    "One star. The Moon shows up late, never replies, and just stares "
    "all night. Worst roommate ever. Would not orbit again."
)

OUTPUT_FILENAME = "review.txt"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
