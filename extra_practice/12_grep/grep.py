#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-04-26
Purpose: Python grep
"""

import argparse
import sys
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Python grep",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("PATTERN", metavar="PATTERN", help="Search pattern")

    parser.add_argument(
        "FILE",
        metavar="FILE",
        type=argparse.FileType("rt"),
        nargs="+",
        help="Input file(s)",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="A readable file",
        metavar="OFILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    parser.add_argument(
        "-i", "--insensitive", help="Case-insensitive search", action="store_true"
    )

    args = parser.parse_args()

    for file in args.FILE:
        if os.path.isfile(file.name):
            file = open(file.name).read().rstrip()
        else:
            parser.error(f"No such file or directory: '{file.name}'")

    return args


# --------------------------------------------------
def main():
    """Python grep"""

    args = get_args()

    if len(args.FILE) > 1:
        for file in args.FILE:
            input = open(file.name).read().rstrip()
            sentences = input.split("\n")
            for line in sentences:
                if args.insensitive == True:
                    if re.search(args.PATTERN.upper(), line.upper()) or re.search(
                        args.PATTERN.lower(), line.lower()
                    ):
                        print(f"{file.name}:{line}", file=args.outfile)
                else:
                    if re.search(args.PATTERN, line):
                        print(f"{file.name}:{line}", file=args.outfile)

    else:
        for file in args.FILE:
            input = open(file.name).read().rstrip()
            sentences = input.split("\n")
            for line in sentences:
                if args.insensitive == True:
                    if re.search(args.PATTERN.upper(), line.upper()) or re.search(
                        args.PATTERN.lower(), line.lower()
                    ):
                        print(line, file=args.outfile)
                else:
                    if re.search(args.PATTERN, line):
                        print(line, file=args.outfile)


# --------------------------------------------------
if __name__ == "__main__":
    main()
