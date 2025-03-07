#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-01
Purpose: Compute GC content
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Compute GC content"""

    parser = argparse.ArgumentParser(
        description="Compute GC content",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # parser.add_argument(
    #    "FILE", metavar="FILE", help="Input sequence file", type=argparse.FileType("rt")
    # )

    # Note that I changed this to allow for a file or stdin
    # also notice that I am using "import sys" above
    parser.add_argument(
        "FILE",
        metavar="FILE",
        type=argparse.FileType("rt"),
        nargs="?",
        default=sys.stdin,
        help="Input sequence file",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Compute GC content"""

    args = get_args()
    file = args.FILE

    # each sequence can be split across multiple lines
    # we will need to compile them into a single string
    # we can do this with a dictionary, where we keep adding the sequence

    ID = ""
    id_to_seq = {}
    highest_gc_content = 0
    highest_gc_id = ""

    for line in file:
        # make this upper case so we can count the number of G's and C's
        seq = line.strip()
        if seq.startswith(">"):
            ID = seq[1:]  # Store the ID without the '>'
            id_to_seq[ID] = ""  # Create an empty string for the sequence
        else:
            id_to_seq[ID] = id_to_seq[ID] + seq.upper()  # Add the sequence to the ID

    for ID in id_to_seq:
        # count the number of G's and C's in the sequence
        seq = id_to_seq[ID]
        gc = seq.count("G") + seq.count("C")
        seq_length = len(seq)
        gc_content = (gc / seq_length) * 100
        if gc_content > highest_gc_content:
            highest_gc_content = gc_content
            highest_gc_id = ID

    print(f"{highest_gc_id} {highest_gc_content:.6f}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
