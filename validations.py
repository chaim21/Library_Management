from i_o import get_input
def is_empty(txt):
    if len(txt.strip()):
        return txt,None
    return False,"cannot except empty str"

def valid_num(num):
    try:
        num = int(num)
        if num > 0:
            return num,None
        return False,"must be a positive num"
    except Exception:
        return False,"must be a positive num"

def valid_book(books):
    name = get_input("enter book name:\n",is_empty)
    author = get_input("enter author book:\n",is_empty)
    for book in books:
            if book["name"].lower() == name.lower() and book["author"].lower() == author.lower():
                print("A book with the same title and author already exists.\n")
                return None,None,None
    year = get_input("Enter publication year\n",valid_num)
    return name,author,year

