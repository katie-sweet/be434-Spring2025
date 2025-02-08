#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-02-08
Purpose: Divide Integers
"""

import argparse


# --------------------------------------------------
def get_args():
                    """Get command-line arguments"""

                    parser = argparse.ArgumentParser(
                        description='Divide Integers',
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

                    parser.add_argument('integer',
                                        metavar='INT',
                                        nargs=2,
                                        type=int,
                                        help='Integers to divide')

                    # parser.add_argument('-a',
                    #'--arg',
                    #help='A named string argument',
                    #metavar='str',
                    #type=str,
                    #default='')

                    #parser.add_argument('-i',
                    #'--int',
                    #help='A named integer argument',
                    #metavar='int',
                    #type=int,
                    #default=0)

                    #parser.add_argument('-f',
                    #'--file',
                    #help='A readable file',
                    #metavar='FILE',
                    #type=argparse.FileType('rt'),
                    #default=None)

                    #parser.add_argument('-o',
                    #'--on',
                    #help='A boolean flag',
                    #action='store_true')

                    return parser.parse_args()


# --------------------------------------------------
def main():
                    """Divide Integers"""

                    args = get_args()
                    integer = args.integer

                    print(f'{integer[0]} / {integer[1]} = {integer[0] // integer[1]}')
                    #if integer[1] == 0:
                        #print('Cannot divide by zero, dum-dum!')
                    #else:
                        #print(f'{integer[0]} / {integer[1]} = {integer[0] // integer[1]}')


# --------------------------------------------------
if __name__ == '__main__':
                    main()
