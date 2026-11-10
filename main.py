from data import books
from book_manage import display_books,search_book
from validations import is_empty
from i_o import get_input



def shoe_menu():
    print('''
    ================================ 
       LIBRARY MANAGEMENT 
    ================================ 
 
    1. Display all books 
    2. Search book by name 
    3. Add new book 
    4. Borrow a book 
    5. Return a book 
    6. Display available books 
    7. Display books by author 
    8. Exit  ''')

def run():
    user_choice = None
    while user_choice != "8":
        shoe_menu()
        user_choice = input("Choose an option:\n")
        match user_choice:
            case "1":
                display_books(books)

            case "2":
                name_book = get_input("enter name of the book:",is_empty)
                books_found = search_book(books,name_book)
                if books_found:
                    display_books(books_found)
                else:
                    print("book not found\n")

run()