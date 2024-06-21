from functions import get_input, get_seq, longest_rep_sub_seq, gc_content

def main():
    args = get_input()
    
    sequence = get_seq(args)

    longest_rep_sub_seq(args, sequence)
    
    gc_content(args, sequence)

main()
