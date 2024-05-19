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
