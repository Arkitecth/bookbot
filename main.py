def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_dict = get_chars_dict(text)
    generate_report(text, book_path)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def char_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_key(dict, value):
    for item in dict:
        if dict[item] == value:
            return item
    return None


def generate_report(text, path):
    print(f"--- Begin report of {path} ---")
    num_words = get_num_words(text)
    char_dict = get_chars_dict(text)
    chars_sorted_list = char_dict_to_sorted_list(char_dict)
    print(f"{num_words} was found in the document")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(
                f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
