#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-09
Purpose: Transcribe DNA to RNA
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
        metavar='file',
        help='Input DNA File',
        type=argparse.FileType("rt"),
        nargs="+",
        default=sys.stdin,)

    parser.add_argument('-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Transcribe DNA to RNA"""

    args = get_args()
    out_dir = args.outdir

    # check if out_dir exists and create it if not
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    #if os.path.isdir(out_dir):
        #out_file = open(out_dir, 'wt')

        # open out file and input file
        for file in args.file:
            out_file = os.path.join(out_dir, os.path.basename(file.name))
        
            # open input file
            input = file.read().rstrip()
            text=' '
            # convert DNA to RNA
            for line in input:
                text = input.replace("T", "U")
                out_dir.write(text)
                #print(f"{text}", file=out_file)

    # print summary to stdout
    if len(args.file) == 1:
        print(f'Done, wrote {len(args.file)} sequence in {len(args.file)} file to directory "{out_dir}".', file=sys.stdout)
        
    else:
        print(f'Done, wrote {len(args.file)} sequences in {len(args.file)} files to directory "{out_dir}".', file=sys.stdout)

    #if os.path.isdir(out_dir):
    #shutil.rmtree(out_dir)
    
    #if os.path.isdir(out_dir):
        #out_file = os.path.join(out_dir, 'input1.txt')
        #out_file = open(out_file, 'wt')
        #out_file.write(text)
        #out_file.close()
    #print('Done, wrote 1 sequence in 1 file to directory "out".', file=sys.stdout)
    

    #out_file.close()


#if os.path.isdir(args.outdir):
#out_fh = open(args.outdir, 'wt') 
#out_fh.write(text + '\n')
#out_fh.close()
#print('Done, wrote 1 sequence in 1 file to directory "out".', file=sys.stdout)

#print(f"{text}", file=output)
#print('Done, wrote 1 sequence in 1 file to directory "out".', file=sys.stdout)


# --------------------------------------------------
if __name__ == '__main__':
    main()
