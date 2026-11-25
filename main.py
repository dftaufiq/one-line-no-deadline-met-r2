#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry (R2).

Writes the single-line excuse to /output/entry.txt (the gate checks that
file: UTF-8 text, 1 to 200 characters) and prints it.
"""

import os

LINE = "Sorry it's late: I did the work in 2 days, then spent day 3 in a meeting about why the work was taking so long, and day 4 writing up that meeting."


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        # Fallback for local runs without permission to create /output.
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
