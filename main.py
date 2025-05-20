def get_book_text(path_to_file):
    file_contents = None

    with open(path_to_file) as file:
        file_contents = file.read()
    
    return file_contents

def count_words(book_text):
    num_of_words = 0

    num_of_words = len(book_text.split())

    return num_of_words

def main():
    num_of_words = count_words(get_book_text("./books/frankenstein.txt"))

    print(f"{num_of_words} words found in the document")

main()
