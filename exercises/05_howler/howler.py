#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-02-22
Purpose: Howler Script
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler Script",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="str", help="Input string or file")

    parser.add_argument(
        "-o", "--outfile", help="Output filename", metavar="str", type=str, default=""
    )

    args = parser.parse_args()

    if os.path.isfile(args.input):
        args.input = open(args.input).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Howler Script"""

    args = get_args()
    input = args.input
    outfile = args.outfile

    if outfile:
        output = open(outfile, "wt")
        print(f"{input.upper()}", file=output)
    else:
        print(input.upper(), file=sys.stdout)


# --------------------------------------------------
if __name__ == "__main__":
    main()
