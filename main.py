import sys


def main():
    book_contents, book_name = read_file()
    print_report(book_contents, book_name)
    num_times_appears(book_contents)


"""
Take in a file as input and return a string containing the contents of the file,
as well as the title of the file/book.

"""
def read_file():
    #Attempt to open the file given by the user
    while True:
        filename = input("Please enter the relative file path to the file you would like to read. \n ")
        if file_exists(filename):
            break
    
    try:
        with open(filename) as file:
            book_contents = file.read()
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

    book_title = get_book_title(filename)
    return book_contents, book_title


"""
Determines if a user provided file exists, and returns false if it does not.
"""
def file_exists(filename):
    try:
        with open(filename) as f:
            pass
    except FileNotFoundError:
        print("File not found.")
        return False
    except Exception as e:
        print("Error:", e)
        return False
    return True



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
Given a word, return the number of times that word occurs in the book
"""
def num_times_appears(book):
    word = input("Which word would you like to search for?\n")
    while not_valid_word(word):
        print("Words can only contain letters of the alphabet and cannot have spaces.")
        word = input("Enter new a word\n")
    #Separate the words in the string into a list
    words = book.split()
    counts = dict()
    for wrd in words:
        counts[wrd.lower()] = counts.get(wrd.lower(), 0) + 1
    
    print(f"The word '{word}' appears {counts.get(word.lower(), 0)} times in this text.\n")


    
"""
Takes in a user-given word and determines if it as a valid word, e.g
no numbers or non-letter chars.
"""
def not_valid_word(word):
    return not word.isalpha()




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