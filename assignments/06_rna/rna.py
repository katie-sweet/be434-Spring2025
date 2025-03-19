#!/usr/bin/env python3
"""
Author : Katie Sweet <kgsweet@arizona.edu>
Date   : 2025-03-09
Purpose: Transcribe DNA to RNA
"""

import argparse
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
        )

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
    num_files, num_seqs = 0, 0
    for file in args.file:
        num_files +=1
        out_file = os.path.join(out_dir, os.path.basename(file.name))
        out_fh = open(out_file, 'wt')

        # open input file
        #input = file.read().rstrip()
        text=' '
        # convert DNA to RNA
        for line in file:
            num_seqs += 1
            out_fh.write(line.replace("T", "U"))
            #text = file.replace("T", "U")
            #out_dir.write()
            #print(f"{text}", file=out_file)
        out_fh.close()

    # print summary to stdout
    if  == 1:
        print(f'Done, wrote {num_seqs} sequence in {num_files} file to directory "{out_dir}".')
        
    else:
        print(f'Done, wrote {num_seqs} sequences in {num_files} files to directory "{out_dir}".')

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
