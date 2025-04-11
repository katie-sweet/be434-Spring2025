#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-04-11
Purpose: Password Maker
"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password Maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs = '+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='min_word_len',
                        type=int,
                        default=4)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='max_word_len',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Password Maker"""

    args = get_args()
    random.seed(args.seed)
    words = set() 

    def word_len(word):                                                     
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word)
    
     words = sorted(words)
    passwords = [
        ''.join(random.sample(words, args.num_words)) for _ in range(args.num)
    ]

    if args.l33t:
        passwords = map(l33t, passwords)

    print('\n'.join(passwords))


# --------------------------------------------------
def clean(word):
    """Remove non-word characters from word"""

    return re.sub('[^a-zA-Z]', '', word)


# --------------------------------------------------
def l33t(text):
    """l33t"""

    text = ransom(text)
    xform = str.maketrans({
        'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'
    })
    return text.translate(xform) + random.choice(string.punctuation)


# --------------------------------------------------
def ransom(text):
    """Randomly choose an upper or lowercase letter to return"""

    return ''.join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text))


# --------------------------------------------------
def test_clean():
    assert clean('') == ''                    
    assert clean("states,") == 'states'       
    assert clean("Don't") == 'Dont'           



# --------------------------------------------------
if __name__ == '__main__':
    main()
