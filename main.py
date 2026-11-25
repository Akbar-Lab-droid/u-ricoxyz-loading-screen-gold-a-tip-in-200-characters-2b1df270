"""Entry program for the u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270 make.fun bounty.

Copies the committed entry.txt to the output directory
(MAKEFUN_OUTPUT_DIR, default "out") as entry.txt.
Standard library only.
"""

# The entry text lives in entry.txt; this program only copies it.

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
