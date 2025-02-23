#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-02-22
Purpose: Print the reverse complement of DNA
"""

import argparse
import os
#from re import A


# --------------------------------------------------
def get_args():
    """Print the reverse complement of DNA"""

    parser = argparse.ArgumentParser(
        description="Print the reverse complement of DNA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("DNA", metavar="str", help="Input sequence or file")

    args = parser.parse_args()

    if os.path.isfile(args.DNA):
        args.DNA = open(args.DNA).read().rstrip()
    return args


# --------------------------------------------------
def main():
    """Print the reverse complement of DNA"""

    args = get_args()
    DNA = args.DNA
    #DNA = DNA.upper()

    DNA_replace = {
                        'A': 'T',
                        'T': 'A',
                        'C': 'G',
                        'G': 'C',
                        'a':'t',
                        't': 'a',
                        'c':'g',
                        'g':'c'
    }
    for char in DNA[::-1]:
        #DNA = DNA_replace.get(char)
        print(f"{DNA_replace.get(char)}", end="")
        
    #DNA_reverse = DNA[::-1]
   # print(f"{DNA_reverse}")

                    


# --------------------------------------------------
if __name__ == "__main__":
    main()

'''
for char in DNA:
                            if char == A:
                                        DNA.replace("A", "t")
                            elif char== t:
                                        DNA.replace("t", "a")
                            elif char == C:
                                        DNA.replace("C", "g")
                            elif char == G:
                                        DNA.replace("G", "c")
    #DNA_replace = DNA.replace("A", "t"), DNA.replace("T", "a"), DNA.replace(
       # "C", "g"), DNA.replace("G", "c")

    for char in DNA:
        if char.upper() == A:
            T = A
        elif char.upper() == T:
            A = T
        elif char.upper() == C:
            G = C
        elif char.upper() == G:
            C = G'''