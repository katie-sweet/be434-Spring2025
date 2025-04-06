#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-04-06
Purpose: Filter Delimited Text File
"""

import argparse
import csv
import sys
import re
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        required = True,
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)
    
    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        required = True,
                        metavar='val',
                        #type=int,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column name for filter',
                        metavar='col',
                        type=str.lower,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')
    
    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    args = parser.parse_args()


    return args


# --------------------------------------------------
def main():
    """Filter Delimited Text File"""

    args = get_args()
    with open(args.file.name, newline = '') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=args.delimiter)
        fieldnames = reader.fieldnames
        #print(fieldnames)
        if args.col:
            if args.col in fieldnames:
                pass
            else:
                print(f'--col "{args.col}" not a valid column!', file=sys.stderr )
                sys.exit(1)
        
        with open(args.outfile.name, mode='w', newline='') as outfile:
            writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            records_written = 0

            for rec in reader:
                text_to_search = []
                if args.col:
                        text_to_search = rec[args.col]
                else:
                        text_to_search = " ".join(rec.values())
        #print(f'{text_to_search}')

                if re.search(args.val, text_to_search, re.IGNORECASE):
                            writer.writerow(rec)
                            records_written += 1
        
            print(f'Done, wrote {records_written} to "{args.outfile.name}".')
        
	

# --------------------------------------------------
if __name__ == '__main__':
    main()
