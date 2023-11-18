def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print_letter_count(text)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count_list(text):
    words = text.replace(" ", "").lower()
    alpha_string = ""
    for letter in words:
        if letter.isalpha():
            alpha_string += letter
    
    letter_dict = {}
    for letter in alpha_string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    tuple_list = list(letter_dict.items())
    tuple_list.sort(key = lambda x: x[1], reverse=True)

    return tuple_list

def print_letter_count(text):
    sorted_list = get_letter_count_list(text)
    for item in sorted_list:
        letter = item[0]
        count = item[1]
        print(f"The '{letter}' character was found {count} times")

    
main()
