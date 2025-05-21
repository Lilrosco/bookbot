from stats import *

def get_book_text(path_to_file):
    file_contents = None

    with open(path_to_file) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_of_words = count_words(book_text)

    print(f"{num_of_words} words found in the document")
    print(count_characters(book_text))

main()
