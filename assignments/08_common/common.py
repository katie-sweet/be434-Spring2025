#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-26
Purpose: Find common words
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find common words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("FILE1", metavar="FILE1", help="Input file 1")

    parser.add_argument("FILE2", metavar="FILE2", help="Input file 2")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    args = parser.parse_args()

    if os.path.isfile(args.FILE1):
        args.FILE1 = open(args.FILE1).read().rstrip()
    else:
        parser.error(f"No such file or directory: '{args.FILE1}'")

    if os.path.isfile(args.FILE2):
        args.FILE2 = open(args.FILE2).read().rstrip()
    else:
        parser.error(f"No such file or directory: '{args.FILE2}'")

    return args


# --------------------------------------------------
def get_words(filehandle):
    """Get words"""

    # return ''.join([f'{filehandle}'])
    return "\n".join([f"{filehandle}"])


# --------------------------------------------------
def main():
    """Find common words"""

    args = get_args()

    input1 = get_words(args.FILE1).split()
    sorted_input1 = sorted(input1)

    input2 = get_words(args.FILE2).split()
    sorted_input2 = sorted(input2)

    text = []

    for word in sorted_input1:
        if word in sorted_input2 and sorted_input1:
            if word in text:
                pass
            else:
                text.append(word)
        else:
            # do nothing
            pass

    for n in text:
        print(n)

# --------------------------------------------------
if __name__ == "__main__":
    main()
