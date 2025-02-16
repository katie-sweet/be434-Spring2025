#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-02-16
Purpose: DNA
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Tetranucleotide frequency",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("DNA", metavar="DNA", help="Input DNA sequence")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Tetranucleotide frequency"""

    args = get_args()
    DNA = args.DNA

    for n in DNA:
        num_A = DNA.count("A")
        num_C = DNA.count("C")
        num_G = DNA.count("G")
        num_T = DNA.count("T")

    # print(DNA)
    # print(num_A, num_C, num_G, num_T)
    print(f"{num_A} {num_C} {num_G} {num_T}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
