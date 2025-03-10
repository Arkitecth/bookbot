from stats import * 
import sys 



def get_book_text(filepath): 
    file = "" 
    with open(filepath) as f: 
        file = f.read()

    return file


def main():
    if len(sys.argv) != 2:
        print("Usage python3 main.py <path_to_book>") 
        sys.exit(1)

    filepath = sys.argv[1] 
    file = get_book_text(filepath)
    num_words = get_count(file) 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    dictionary = get_character_count(file)
    sorted_list = sort_dictionary(dictionary)
    for item in sorted_list: 
        for key, val in item.items():
            print(f"{key}: {val}") 
    print("============= END ===============")
    
main()
