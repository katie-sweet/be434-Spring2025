#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-04-11
Purpose: Find conserved bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find conserved bases",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file", metavar="FILE", type=argparse.FileType("rt"), help="Input file"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Find conserved bases"""

    args = get_args()

    seqs = [line.strip() for line in args.file if line.strip()]

    for seq in seqs:
        print(seq)

    conserved = ""
    for i in range(len(seqs[0])):
        chars = set(seq[i] for seq in seqs)
        conserved += "|" if len(chars) == 1 else "X"

    print(conserved)


# --------------------------------------------------
if __name__ == "__main__":
    main()
