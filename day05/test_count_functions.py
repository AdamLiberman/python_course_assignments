from functions import characters_counter, lines_counter, words_counter

def test_characters_counter():
    with open("testing_file_1.txt") as text_1:
        assert characters_counter(text_1.readlines()) == 22
    with open("testing_file_2.txt") as text_2:
        assert characters_counter(text_2.readlines()) == 23

def test_lines_counter():
    with open("testing_file_1.txt") as text_1:
        assert lines_counter(text_1.readlines()) == 1
    with open("testing_file_2.txt") as text_2:
        assert lines_counter(text_2.readlines()) == 3

def test_words_counter():
   with open("testing_file_1.txt") as text_1:
        assert words_counter(text_1.readlines()) == 5
   with open("testing_file_2.txt") as text_2:
        assert words_counter(text_2.readlines()) == 6
