#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-26
Purpose: Sing Bottles of Beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sing Bottles of Beer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of verses',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def verse(bottle):
    '''Sing verses'''

    next_bottle = bottle-1
    s1 = '' if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    next_num = next_bottle if bottle != 1 else 'No more'
    #next_num = 'No more' if next_bottle == 0 else next_bottle

    return '\n'.join([
            f'{bottle} bottle{s1} of beer on the wall,\n'
            f'{bottle} bottle{s1} of beer,\n'
            'Take one down, pass it around,\n'
            f'{next_num} bottle{s2} of beer on the wall!'])


# --------------------------------------------------
def test_verse():
    '''Test verse'''

    one = verse(1)
    assert one == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two = verse(2)
    assert two == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'
    ])

# --------------------------------------------------
def main():
    """Sing Bottles of Beer"""

    args = get_args()
    
    # Solution using for loop
    #verses = []
    #for n in range(args.num, 0, -1):
        #verses.append(verse(n))

    #print('\n\n'.join(verses))

    # Solution using list comprehension
    verses = [verse(n) for n in range(args.num, 0, -1)]
    print('\n\n'.join(verses))

    # See solution.py for solution using 'map'
# --------------------------------------------------
if __name__ == '__main__':
    main()
