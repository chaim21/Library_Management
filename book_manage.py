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
