from stats import word_count
from stats import char_count

def main():
    text = get_book_text("books/frankenstein.txt")
    words = word_count(text)
    characters = char_count(text)
    #L3: print(get_book_text("books/frankenstein.txt"))
    #L4: print(f"{word_count(text)} words found in the document")
    print(words)
    print(characters)

def get_book_text(relative_path):
    file_contents = ""
    with open(relative_path) as f:
        file_contents = f.read()
    return file_contents

main()
