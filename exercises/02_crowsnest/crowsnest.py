#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-02-02
Purpose: Crowsnest: Choose the Article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the Article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='object',
                        help='Thing we see')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Crowsnest"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    #print('Ahoy, Captain, ' + article + args.word + ' off the larboard bow!')
    #print('Ahoy, Captain, {} {} off the larboard bow!'. format(article, word))
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
                    

# --------------------------------------------------
if __name__ == '__main__':
    main()
