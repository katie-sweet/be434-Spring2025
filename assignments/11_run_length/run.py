#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-21
Purpose: Add Your Purpose
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Run-length encoding/data compression",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="DNA text or file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def rle(seq):
    """Create RLE (Run-Length Encoding) string"""

    if not seq:
        return ""

    result = []
    count = 1
    prev_char = seq[0]

    for char in seq[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(f'{prev_char}{count if count > 1 else ""}')
            prev_char = char
            count = 1

    result.append(f'{prev_char}{count if count > 1 else ""}')  # Final group

    return "".join(result)


# --------------------------------------------------
def test_rle():
    """Test rle"""

    assert rle("A") == "A"
    assert rle("ACGT") == "ACGT"
    assert rle("AA") == "A2"
    assert rle("AAAAA") == "A5"
    assert rle("ACCGGGTTTT") == "AC2G3T4"
    assert rle("") == ""
    assert rle("AABBA") == "A2B2A"


# --------------------------------------------------
def main():
    """Run-length encoding/data compression"""

    args = get_args()
    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
if __name__ == "__main__":
    main()
