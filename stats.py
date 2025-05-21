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
