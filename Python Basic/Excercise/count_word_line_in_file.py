def count_words_lines_of_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            print(lines)
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            print(f"Number of line: {line_count}")
            print(f"Number of word: {word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found!!!")
        
count_words_lines_of_file("sample.txt")