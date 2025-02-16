#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-02-16
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Jump the Five"""

    args = get_args()
    input = args.input

    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    for char in input:
        if char in jumper:
            print(f"{jumper.get(char)}", end="")
        else:
            print(f"{char}", end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
