#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-01-25
Purpose: Say Hello
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say Hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='Name to greet',
                        metavar='name',
                        type=str,
                        default='World')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Say Hello"""

    args = get_args()

    print("Hello, " + args.name +"!")
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
