#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-01
Purpose: Compute GC content
"""

import argparse
import sys
from typing import TYPE_CHECKING


# --------------------------------------------------
def get_args():
    """Compute GC content"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input sequence file',
                        type=argparse.FileType('rt'))

 
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Compute GC content"""

    args = get_args()
    file = args.FILE

    for fh in file:
      gc = 0
      for line in fh:
                          if char[0] == '<' :
                                              ID = line[1:]
                          else:
                                              seq = line.strip()
                                              gc = gc + seq.count('G') + seq.count('C')
                                              gc_content = gc / len(seq) * 100
                                              print(f'{ID} {gc_content:.1f}')

# --------------------------------------------------
if __name__ == '__main__':
    main()

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
