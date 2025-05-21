from stats import *

def get_book_text(path_to_file):
    file_contents = None

    with open(path_to_file) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    book_location = "./books/frankenstein.txt"
    book_text = get_book_text(book_location)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    num_of_words = count_words(book_text)
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    print(
        pretty_print_character_stats(
            sorted_character_stat(
                count_characters(book_text)
            )
        )
    )
    print("============= END ===============")

main()
