import sys
from functions import characters_counter, lines_counter, words_counter

def input_file():
    if len(sys.argv) !=2:
        exit("Usage: {sys.argv[0]} FILENAME")
    
    filename = sys.argv[1]
    return(filename)

def print_count(number_of_characters, number_of_lines, number_of_words):
    print(f"number of characters: {number_of_characters}")
    print(f"nubmer of lines: {number_of_lines}")
    print(f"nubmer of words: {number_of_words}")

def main():
    filename = input_file()

    with open(filename) as fh:
        text = fh.readlines()
        number_of_characters = characters_counter(text)
        number_of_lines = lines_counter(text)
        number_of_words = words_counter(text)
        
    print_count(number_of_characters, number_of_lines, number_of_words)
        
main()