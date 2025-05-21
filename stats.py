def count_words(book_text):
    num_of_words = 0
    num_of_words = len(book_text.split())

    return num_of_words

def count_characters(book_text):
    character_count_dict = dict()

    for word in book_text:
        for character in word.lower().split(" "):
            if character in character_count_dict:
                character_count_dict[character] = character_count_dict[character] + 1
            else:
                character_count_dict[character] = 1
    
    return character_count_dict

def sort_on(dict):
    return dict["num"]

def sorted_character_stat(char_dict):
    sorted_char_dict = []

    # Iterate by key which is the char
    for char in char_dict:
        if char.isalpha():
            sorted_char_dict.append({"char": char, "num": char_dict[char]})
    
    sorted_char_dict.sort(reverse=True, key=sort_on)
    
    return sorted_char_dict

def pretty_print_character_stats(sorted_char_dict):
    prettified_str = ""
    current_char = None
    current_char_count = None

    for dict in sorted_char_dict:
        current_char = dict["char"]
        current_char_count = dict["num"]
        prettified_str += f"{current_char}: {current_char_count}\n"
    
    return prettified_str
