#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-02-02
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Print greeting",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-g",
        "--greeting",
        help="The greeting",
        metavar="greeting",
        type=str,
        default="Howdy",
    )
    parser.add_argument(
        "-n", "--name", help="Whom to greet", metavar="name", default="Stranger"
    )
    parser.add_argument(
        "-e", "--excited", help="Include a exclamation point", action="store_true"
    )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print greeting"""

    args = get_args()
    excited = "!" if args.excited == True else "."

    print(args.greeting + ", " + args.name + excited)


# --------------------------------------------------
if __name__ == "__main__":
    main()
