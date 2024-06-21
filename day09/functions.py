import argparse
import re
from Bio import SeqIO

def gc_content(args, sequence):
    if args.gc_content:
        matches = re.findall(r'[GC]{1}', sequence)
        print(len(matches)*100/len(sequence))

def longest_rep_sub_seq(args, sequence):
    if args.duplicate:
        length = 1
        result = ''
        while True:
            regex = r'([GATC]{' + str(length) + r'}).*\1'
            m = re.search(regex, sequence)
            if m:
                result = m.group(1)
                length += 1
            else:
                break
        print(result)

def get_seq(args):
    for seq_record in SeqIO.parse(args.FILE, "fasta"):
       sequence = str(seq_record.seq)
    return sequence

def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', help= 'Path to sequence file')
    parser.add_argument('--duplicate', action = 'store_true', help= 'Show longest repeating sub-sequence of the sequence')
    parser.add_argument('--gc_content', action = 'store_true', help= 'Show GC content of the sequence')
    args = parser.parse_args()
    return args
