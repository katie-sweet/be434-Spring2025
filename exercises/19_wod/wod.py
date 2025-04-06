#!/usr/bin/env python3
"""
Author : Katie <kgsweet@arizona.edu>
Date   : 2025-04-04
Purpose: Generate Workout
"""

import argparse
import random
import csv
from pprint import pprint
import io
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create workout',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""
    exercises = []                                                       
    for row in csv.DictReader(fh, delimiter=','):                        
        low, high = map(int, row['reps'].split('-'))                     
        exercises.append((row['exercise'], low, high))                   
 
    return exercises    
    
    '''reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        repstr = reps.split('-')
        low, high = int(repstr[0]), int(repstr[1])
        numreps = random.randint(low, high)
        exercises.append((name, low, high))

    return exercises'''


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]

# --------------------------------------------------
def main():
    """Create workout"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
    wod = []

    for name, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps / 2)
        wod.append((name, reps))


    print(tabulate(wod, headers = ('Exercise', 'Reps')))


# --------------------------------------------------
if __name__ == '__main__':
    main()
