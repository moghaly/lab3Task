import time
from filehandler import saveBook, getAll, searchID,\
    updateBooksDB, deleteFromFile
def enterStr(msg):
    mystr=input("please enter "+msg)
    if mystr=="" or mystr.isspace():
        print("==========please provide a string value!=============")
        return enterStr(msg)
    return mystr
def enterNum(msg):
    myNum=input("please enter "+msg)
    try:
        myNum=int(myNum)
        return myNum
    except:
        print("=========please provide a number of type integer!==========")
        return enterNum(msg)
def inputDetails():
        title=enterStr("title: ")
        author=enterStr("author: ")
        pagesNum=enterNum("number of pages: ")
        pagesNum=str(pagesNum)
        return title, author, pagesNum

def createBook():
        bDetails=inputDetails()
        bDetails=list(bDetails)
        id=genNewID()
        id=str(id)
        bDetails.insert(0,id)
        bookDetails=":".join(bDetails)
        print(bookDetails)
        saved=saveBook(bookDetails)
        if saved:
            print("book saved successfully..")
        else:
            print("====error occurred, we are sorry for that!, please try again.")
            return createBook

def genNewID():
    id=round(time.time())
    return id
def listAll():
    data= getAll()
    chk=data[0]
    info=data[1]
    #info=info.split("\n")
    if chk:
        for x in list(info):
            print(x)
    else:
        print("No available Data!")
def updateBook():
    print("=======Listing all entries=======\n"
          "=====selection for update based on "
          "ID(1st element)=======")
    listAll()
    bID=enterNum("ID of the book u want to edit: ")
    data=searchID(bID)
    print(data)
    chk=data[0]
    if chk:
        myBKindex=data[1]
        print(f"this entry will be edited:\n{data[2]}")
        newDetail=list(inputDetails())
        newDetail.insert(0, str(bID))
        newDetail=":".join(newDetail)
        #print(newDetail)
        updateBooksDB(myBKindex, newDetail)
def deleteEntry():
    print("listing all Books to choose one(based on ID) for deletion:")
    listAll()
    bookID=enterNum("ID of book u want to delete: ")
    deleted= deleteFromFile(bookID)
    if deleted:
        print("book deleted successfully..")
