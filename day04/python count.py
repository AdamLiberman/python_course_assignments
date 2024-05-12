import sys


def characters_counter(filename):
    num_chr = 0
    with open(filename) as fh:
        for line in fh:
            line = line.rstrip()
            for ch in line: 
                num_chr +=1
    return(num_chr)

def lines_counter(filename):
    num_lines = 0
    with open(filename) as fh:
        for line in fh:
         num_lines +=1
    return(num_lines)

def words_counter(filename):
    num_words = 0
    with open(filename) as fh:
        text = fh.read()
        for line in fh:
            line = line.rstrip()
            for ch in line: 
                if str == ch + " " + ch:
                    num_words +=1
    return(num_words)

def main():
    if len(sys.argv) !=2:
        exit("Usage: {sys.argv[0]} FILENAME")
    
    filename = sys.argv[1]
    numer_of_characters = characters_counter(filename)
    print(f"number of characters: {numer_of_characters}")
    numer_of_lines = lines_counter(filename)
    print(f"nubmer of lines: {numer_of_lines}")
    number_of_words = words_counter(filename)
    print(f"nubmer of words: {number_of_words}")
main()