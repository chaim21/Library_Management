def display_books(books:list):
    for book in books:
        print([(key,value) for key,value in book.items()])
