import sys


def characters_counter(text):
    num_chr = 0
    for line in text:
        line = line.rstrip()
        num_chr += len(line)
    return(num_chr)

def lines_counter(text):
    num_lines = 0
    for line in text:
         num_lines +=1
    return(num_lines)

def words_counter(text):
    num_words = 0
    for line in text:
        num_words += len(line.split())
    return(num_words)

def main():
    if len(sys.argv) !=2:
        exit("Usage: {sys.argv[0]} FILENAME")
    
    filename = sys.argv[1]
    with open(filename) as fh:
        text = fh.readlines()
        number_of_characters = characters_counter(text)
        print(f"number of characters: {number_of_characters}")
        number_of_lines = lines_counter(text)
        print(f"nubmer of lines: {number_of_lines}")
        number_of_words = words_counter(text)
        print(f"nubmer of words: {number_of_words}")
main()