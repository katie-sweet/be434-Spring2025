#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-01
Purpose: Compute GC content
"""

import argparse


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

    highest_gc_content = 0.0
    highest_gc_id = ""
    ID = ''
    for line in file:
                        seq = line.strip()
                        if seq.startswith('>'):
                                            ID = seq[1:]  # Store the ID without the '>'
                        else:
                                            gc = 0 + seq.count('G') + seq.count('C')
                                            gc_content = gc / len(seq.strip()) * 100
                                            if gc_content > highest_gc_content:
                                                                highest_gc_content = gc_content
                                                                highest_gc_id = ID
    print(f'{highest_gc_id} {highest_gc_content:.6f}')

    
               

# --------------------------------------------------
if __name__ == '__main__':
    main()



               