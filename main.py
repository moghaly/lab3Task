from book_ops import createBook, listAll, updateBook, deleteEntry

"""
    console application for library
    add , edit , delete , display information of the books
    create:
        title , no_of_pages, author_name
"""


def mainmenu():
    sel = input("please enter (c) to create new book, "
                "(l) to list all available books, "
                "(u) to update an existing book, "
                "(d) to delete a book ")
    if sel == "c":
        print("creating new book")
        createBook()

    elif sel == "l":
        print("=============Listing all books=========")
        listAll()
    elif sel == "u":
        print("updating a book")
        updateBook()
    elif sel == "d":
        print("deleting a book")
        deleteEntry()
    else:
        print("==========please provide a correct selection!=========")
        return mainmenu()


while True:
    mainmenu()
