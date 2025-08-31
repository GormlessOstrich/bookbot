import sys
from stats import word_count
from stats import char_count
from stats import dict_sort

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    words = word_count(text)
    characters = char_count(text)
    sorted_list = dict_sort(characters)
    #L3: print(get_book_text(book))
    #L4: print(f"{word_count(text)} words found in the document")
    #print(words)
    #print(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(relative_path):
    file_contents = ""
    with open(relative_path) as f:
        file_contents = f.read()
    return file_contents

main()
