#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-19
Purpose: Create synthetic sequences
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Create synthetic sequences",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="outfile",
        type=argparse.FileType("at"),
        default="out.fa",
    )

    parser.add_argument(
        "-t",
        "--seqtype",
        help="DNA or RNA",
        metavar="seqtype",
        choices=["dna", "rna"],
        type=str,
        default="dna",
    )

    parser.add_argument(
        "-n",
        "--numseqs",
        help="Number of sequences to create",
        metavar="numseqs",
        type=int,
        default=10,
    )

    parser.add_argument(
        "-m", "--minlen", help="Minimum length", metavar="minlen", type=int, default=50
    )

    parser.add_argument(
        "-x", "--maxlen", help="Maximum length", metavar="maxlen", type=int, default=75
    )

    parser.add_argument(
        "-p", "--pctgc", help="Percent GC", metavar="pctgc", type=float, default=0.5
    )

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args


# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """Create the pool of bases"""

    t_or_u = "T" if seq_type == "dna" else "U"
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = "A" * num_at + "C" * num_gc + "G" * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return "".join(sorted(pool))


# --------------------------------------------------
def main():
    """Synthetic sequences"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    
    for sequence in range(0, args.numseqs):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = random.sample(pool, seq_len)
        
        #with open(args.outfile.name, "a") as myfile:
            #myfile.write(f">{sequence+1}\n{''.join(seq)}\n")

        args.outfile.write(f'>{sequence+1}\n{''.join(seq)}\n')

    print(
        f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile.name}".'
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
