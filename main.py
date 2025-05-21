from stats import *
import sys

def get_book_text(path_to_file):
    file_contents = None

    with open(path_to_file) as file:
        file_contents = file.read()
    
    return file_contents

def print_report(book_location, num_of_words, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    print(
        pretty_print_character_stats(
            sorted_char_list
        )
    )
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Missing arguments")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_location = sys.argv[1]
    book_text = get_book_text(book_location)
    num_of_words = count_words(book_text)
    sorted_char_list = sorted_character_stat(count_characters(book_text))

    print_report(book_location, num_of_words, sorted_char_list)

main()
