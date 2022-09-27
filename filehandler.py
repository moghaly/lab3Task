def saveBook(bookDetails):
    try:
        DBobj=open("booksDB.txt","a")
        DBobj.write(f"{bookDetails}\n")
        return True
    except:
        print("======error while creating, we are sorry for that, please try again.======")
        return False
def getAll():
    try:
        DBobj=open("booksDB.txt")
        data=DBobj.readlines()
        DBobj.close()
       # print(data)
        return True, data
    except:
        print("Development Error: please chk u r in the right env, right dir, and that the database file exist!!!")
        return False
def searchID(bID):
    data=getAll()
    print("======================================"+str(data[1]))
    if data[0]:
        books=data[1]
       # print(data[1])
        for bk in books:
            myBook=bk.strip("\n")
            myBook=myBook.split(":")
            print(myBook)
            if myBook[0]==str(bID):
                myBookIndex=books.index(bk)
                print(myBookIndex)
                return True, myBookIndex, myBook
        else:
            print("Book Not found!!")
            return False
def updateBooksDB(bookIndex, data):
    raw=getAll()
    if raw[0]:
        books=raw[1]
        books[bookIndex]=f"{data}\n"
        updated=updateFile(books)
        if updated:
            print("Database updated successfully.")
def updateFile(books):
    try:
        DBobj=open("booksDB.txt","w")
        DBobj.writelines(books)
        DBobj.close()
        return True
    except Exception:
      print(Exception)
      return False
def deleteFromFile(bookID):
    raw=searchID(bookID)
    exist=raw[0]
    if exist:
        index=raw[1]
        raw=getAll()
        books=raw[1]
        del books[index]
#       books=list[books]
        chk=updateFile(books)
        return chk
