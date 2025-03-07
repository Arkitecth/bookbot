def get_book_text(filepath): 
    file = "" 
    with open(filepath) as f: 
        file = f.read()
    return file




def main():
    file = get_book_text("./books/frankenstein.txt")
    print(file)

main()
