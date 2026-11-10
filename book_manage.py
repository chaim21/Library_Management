from data import books
def display_books(books:list):
    for book in books:
        dispaly_book(book)

def search_book(books, name):
    find_book = []
    for book in books:
        if book["name"].lower() == name.lower():
            find_book.append(book)
    if find_book:
        return find_book

def dispaly_book(book:dict):
    print(f'''
    id: {book["id"]}
    name: {book["name"]}
    author: {book["author"]}
    year: {book["year"]}
    available: {book[ "available"]}
''')

def add_book(books, name, author, year):
    new_book = {"id": get_next_id(books), "name": name, "author": author, "year": year, "available":True}
    books.append(new_book)
    return True


def get_next_id(books:list):
    new_id = max(books,key = lambda i : i["id"])
    return new_id["id"] + 1

def borrow_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return True,"The book was successfully borrowed."
            else:
                return False,"The book is already checked out."
    return False,"book not exists"

def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                return True,"The book was returned successfully."
            else:
                return False,"An existing book cannot be returned."
    return False,"book not exists"

def get_available_books(books):
    available = []
    for book in books:
        if book["available"]:
            available.append(book)
    return available
