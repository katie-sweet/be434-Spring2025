#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-09
Purpose: Apples and Bananas
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='Input text or file')
                        #type=argparse.FileType('rt'),
                        #default=sys.stdin)

    parser.add_argument("-v", "--vowel", help="The vowel to substitute", metavar="str", type=str, default="a", choices=list('aeiou')
                       )

    args = parser.parse_args()
    
    if os.path.isfile(args.input):
                        args.input = open(args.input).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.input
    vowel = args.vowel

    for char in 'aeiou':
                        input = input.replace(char, vowel).replace(char.upper(), vowel.upper())
                    
    print(f"{input}")


# --------------------------------------------------
if __name__ == '__main__':
    main()




 if os.path.isfile(args.file):
                        args.file = open(args.file).read().rstrip()


    return args



 parser.add_argument('file',
                        metavar='FILE',
                        help='Input DNA File',
                        nargs='+')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    # Check if files exist, and read their content
    for file in args.file:
                    if os.path.isfile(file):
                                        args.file[args.file.index(file)] = open(file).read().rstrip()
                    else:
                        print(f"No such file or directory:{file}")
    return args

## 9:05 PM
 args = get_args()
    file = args.file
    outdir = args.outdir
    output = open(outdir, "wt")

    file_replace = {
                            "A": "A",
                            "T": "U",
                            "C": "C",
                            "G": "G",
                            "a": "a",
                            "t": "u",
                            "c": "c",
                            "g": "g",
                        }

    for char in file:
                            #print(f"{file_replace.get(char)}", end="", file=output)
                        print(f"{file}")
                        print(f"{file_replace.get(char)}", end="", file=sys.stdout)
                            #print("Done, wrote 1 sequence in 1 file to directory 'out'.", file = sys.stdout)








for char in file:

        if char in file_replace:
            print(f"{file_replace.get(char)}", end="")
        else:
            print(f"{char}", end="")






                            file_replace = {
                                                        "A": "A",
                                                        "T": "U",
                                                        "C": "C",
                                                        "G": "G",
                                                        "a": "a",
                                                        "t": "u",
                                                        "c": "c",
                                                        "g": "g",
                                                    }

                              '''  for char in file:
                                    print(f"{file_replace}")
                                    print(f"{file_replace.get(char)}", end="", file=sys.stdout)
                                    print('Done, wrote 1 sequence in 1 file to directory "out".', file=sys.stdout)'''





 args = get_args()
    file = args.file
    outdir = args.outdir
    output = open(outdir, "wt")

    text = ''
    for line in file:
        seq = line.strip()
        for seq in file:
            text = text + seq.replace("T", "U")
    print(f"{text}")