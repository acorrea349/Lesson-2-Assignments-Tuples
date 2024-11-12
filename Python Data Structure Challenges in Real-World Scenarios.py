# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update 
# this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

def add_books(library):
    title = input("Enter the title of the book you wish to add: ").lower().title()
    author = input("Enter the name of the author of the book you wish to add: ").lower().title()
    new_library = list(library)
    new_library.append((title, author))
    return tuple(new_library)

def show_books(library):
    print("Current books in the library are:")
    if not library:
        print("No books available.")
    else:
        for title, author in library:
            print(f"{title} by {author}.")

def existing_library():
    
    
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    
    while True:

        try:

            user_input = int(input("Would you like to add a book to the library (1.yes/ 2.no) "))
            if user_input == 1: 
                library = add_books(library)                                 
            
            elif user_input == 2:
                print(" ")
                break
            
            else:
                print("Please input 1 or 2.")

        except ValueError:
            print("Invalid Input. Please enter valid interger")

        

    show_books(library)



existing_library()
print("Thank you for using the Library App")