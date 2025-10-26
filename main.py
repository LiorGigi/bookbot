import sys
from stats import num_of_words
from stats import char_count
from stats import num_of_words, sort_characters


def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = num_of_words(text)

    c_count = char_count(text)
    print(c_count)
    
    sorted_counts = sort_characters(c_count)
    # ----- report -----
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()

        