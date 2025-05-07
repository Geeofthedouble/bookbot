from stats import count_words

from stats import count_chars

from stats import sort_chars

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return(file_contents)

def main():
    
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_chars = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

  # Print each alphabetical character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
            
    print("============= END ===============")  

main()