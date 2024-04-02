def main():

    selected_book = "books/frankenstein.txt"

    with open(selected_book) as file:
        book_contents = file.read()

    book_name = get_book_title(selected_book)
    print_report(book_contents, book_name)

"""
Takes in a book file path and returns only the name of the .txt file in the path
"""
def get_book_title(book_path):
    left_cutoff = 0
    #Removes the file path from the book.txt file
    while book_path[left_cutoff] != "/":
        left_cutoff += 1

    right_cutoff = left_cutoff + 1
    #Removes the ".txt." from the file
    while book_path[right_cutoff] != ".":
        right_cutoff += 1

    return book_path[left_cutoff + 1 : right_cutoff]

"""
Takes in a book string as input and returns how many words are in the book
"""
def count_words(book):
    num_words = len(book.split())

    return num_words

"""
Takes in a book string as input and returns a dictionary containing 
the counts of each letter in the book
"""
def count_letters(book):
    counts = dict()
    for c in book:
        counts[c.lower()] = counts.get(c.lower(), 0) + 1

    return counts

"""
Takes a string book as input and gives a summary of the number of words, 
and number of each letter in the book
"""
def print_report(book, book_title):
    print(f"----- Start report of {book_title} -----")
    print(f"There are {count_words(book)} words in this book")
    print("\n")
     
    book_dict = count_letters(book)
    #Sort the dictionary from highest char count to lowest
    sorted_book_dict = dict(sorted(book_dict.items(), key=lambda item: item[1], reverse=True))
    
    #Print each char count for letters only
    for c, count in sorted_book_dict.items():
        if c.isalpha():
            print(f"The char '{c}' appears {count} times")
        
    print("----- End Report -----")



main()