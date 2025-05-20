def get_book_text(path_to_file):
    file_contents = None

    with open(path_to_file) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()
