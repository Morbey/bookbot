import sys
from sys import argv
from stats import get_words_count, get_character_dict, sort_on_dict

def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        file_contents = f.read()
        book_text += file_contents
    return book_text

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_words_count = get_words_count(book_text)
    book_characters_dict = get_character_dict(book_text)
    sorted_characters_list = sort_on_dict(book_characters_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_characters_list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")



main()