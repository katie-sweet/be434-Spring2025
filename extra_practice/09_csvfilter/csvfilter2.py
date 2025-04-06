#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-06
Purpose: Add Your Purpose
"""

import argparse
import csv
import re
import sys

def filter_csv(args):
    # Open the input file
    with open(args.file, mode='r', newline='', encoding='utf-8') as infile:
        # Create a CSV DictReader to read the file
        reader = csv.DictReader(infile, delimiter=args.delimiter)

        # If a column is provided, check if it is valid
        if args.col and args.col not in reader.fieldnames:
            print(f'--col "{args.col}" not a valid column!', file=sys.stderr)
            print(f'Choose from {", ".join(reader.fieldnames)}', file=sys.stderr)
            sys.exit(1)

        # Prepare the output file for writing
        with open(args.outfile, mode='w', newline='', encoding='utf-8') as outfile:
            # Create a CSV DictWriter for the output file
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            # Initialize a counter for the number of records written
            records_written = 0

            # Loop through each record in the CSV file
            for rec in reader:
                # Determine which value to search for
                if args.col:
                    text_to_search = rec[args.col]
                else:
                    text_to_search = " ".join(rec.values())  # Search all columns

                # Perform the case-insensitive search
                if re.search(args.val, text_to_search, re.IGNORECASE):
                    # If there's a match, write the record to the output file
                    writer.writerow(rec)
                    records_written += 1

            # Inform the user how many records were written
            print(f'Done, wrote {records_written} to "{args.outfile}".')

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Filter delimited records")
    parser.add_argument('-f', '--file', required=True, help="Input file (default: None)")
    parser.add_argument('-v', '--val', required=True, help="Value for filter (default: None)")
    parser.add_argument('-c', '--col', help="Column name for filter (default: )")
    parser.add_argument('-o', '--outfile', default='out.csv', help="Output filename (default: out.csv)")
    parser.add_argument('-d', '--delimiter', default=',', help="Input delimiter (default: ,)")
    
    # Parse the arguments
    args = parser.parse_args()

    # Call the function to filter and write the CSV
    filter_csv(args)

if __name__ == "__main__":
    main()





  '''  Katie draft:
    # --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""
    #with open(fh) as csvfile:
    reader = csv.DictReader(fh, delimiter=args.delimiter)
    fieldnames = reader.fieldnames
    print(fieldnames)
    if args.col in fieldnames:
        pass
    else:
        parser.error(f'--col "{args.col}" not a valid column!', file=sys.stderr )
        sys.exit(1)
    
    return fieldnames '''



    