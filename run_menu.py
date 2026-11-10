from data import books
from book_manage import display_books, search_book, get_next_id, add_book, borrow_book, get_available_books, return_book, get_books_by_author
from validations import is_empty, valid_book, valid_num
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

            case "3":
                name,author,year = valid_book(books)
                if name:
                    add_book(books,name,author,year)
                    print("The book was added successfully.")
                    
            case "4":
                book_id = get_input("Enter the ID of the book to be borrowed:\n",valid_num)
                borrow,msg = borrow_book(books,book_id)
                print(msg)

            case "5":
                book_id = get_input("Enter the ID of the book to be returned:\n",valid_num)
                returned,msg = return_book(books,book_id)
                print(msg)

            case "6":
                available_books = get_available_books(books)
                if available_books:
                    display_books(available_books)
                else:
                    print("No books available")

            case "7":
                author = get_input("Enter the author's name\n",is_empty)
                found = get_books_by_author(books,author)
                if found:
                    display_books(found)
                else:
                    print("There is no author with this name.")

            case _:
                print("please choose a number between 1-8")

