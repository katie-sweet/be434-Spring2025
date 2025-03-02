#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-10-04
Purpose: Emulate wc (word count)
"""

import argparse
import sys
from typing import TYPE_CHECKING


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        nargs='*')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Emulate wc (word count)"""

    args = get_args()
    total_lines = 0
    total_words = 0
    total_chars = 0

    for fh in args.files:
        num_lines = 0
        num_words = 0
        num_chars = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)

        print('{:>8}{:>8}{:>8} {}'.format(num_lines, num_words, num_chars,
                                          fh.name))

        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars

    if len(args.files) > 1:
        print('{:>8}{:>8}{:>8} total'.format(total_lines, total_words,
                                             total_chars))


# --------------------------------------------------
if __name__ == '__main__':
    main()


# For cgc.py:
'''for fh in file:
    gc = 0
    for line in fh:
                        if char[0] == '<' :
                                            ID = line[1:]
                        else:
                                            seq = line.strip()
                                            gc = gc + seq.count('G') + seq.count('C')
                                            gc_content = gc / len(seq) * 100
                                            print(f'{ID} {gc_content:.1f}')'''

 ''' for line in file:
           seq = line.strip()
           if seq:  # Check if the line is not empty
               gc = seq.count('G') + seq.count('C')
               gc_content = gc / len(seq) * 100
               print(f'{seq[:10]} {gc_content:.1f}')  # Display an identifier and GC content'''

for line in file:
           seq = line.strip()
           if seq[0] == '>':
                               ID = seq[1:]
           else:
               gc = seq.count('G') + seq.count('C')
               gc_content = gc / len(seq) * 100
               #print(f'{ID} {gc_content:.6f}')


# 5:58pm
for line in file:
    seq = line.strip()
    if seq[0] == '>':
                        ID = seq[1:]

    else:
                        gc = seq.count('G') + seq.count('C')
                        gc_content = gc / len(seq) * 100
    for i in file:
                          if ID[i+1] > ID[i]:
                                              ID = ID[i+1]
                          else:
                                              ID = ID[i]
                          if ID[i+2] > ID[i+1]:
                                              ID = ID[i+2]
                          else:
                                              ID = ID[i+1]
    print(f'{ID} {gc_content:.6f}')


# 6:34pm
highest_gc_content = 0.0
highest_gc_id = ""
for line in file:
                    seq = line.strip()
                    #seq = line
                    if seq.startswith('>'):
                            ID = seq[1:]  # Store the ID without the '>'
                    else:
                                        gc = 0 + seq.count('G') + seq.count('C')
                                        gc_content = gc / len(seq.strip()) * 100
                                        if gc_content > highest_gc_content:
                                                            highest_gc_content = gc_content
                                                            highest_gc_id = ID
print(f'{highest_gc_id} {highest_gc_content:.6f}')