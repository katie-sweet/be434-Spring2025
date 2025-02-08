#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-02-07
Purpose: Picnic Exercise with Lists
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Items we are bringing')
   
    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Picnic Game"""

    args = get_args()
    items = args.items
    num = len(items)
    #print(args.items)
    if num == 1:
        print(f"You are bringing {items[0]}.")
    elif num == 2:
        if args.sorted == True:
            alphabetical = sorted(items)
            print(f"You are bringing {alphabetical[0]} and {alphabetical[1]}.")
        else:
            print(f"You are bringing {items[0]} and {items[1]}.")
    else:
        if args.sorted == True:
            alphabetical = sorted(items)
            print(f"You are bringing {', '.join(alphabetical[:-1])}, and {alphabetical[-1]}.")
        else:
            print(f"You are bringing {', '.join(items[:-1])}, and {items[-1]}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
