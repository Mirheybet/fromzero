#!/usr/bin/env python3
class Book:
    def __init__(self,title=None,author=None,isborrow=False):
        self.title = title
        self.author = author
        self.isborrow = isborrow
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self,title):
        if  isinstance(title,str):
            self.__title = title
        else:
            raise ValueError("TITLE must be str")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self,author):
        if  isinstance(author,str):
            self.__author = author
        else:
            raise ValueError("AUTHOR must be str")
    
    @property
    def isborrow(self):
        return self.__borrow

    @isborrow.setter
    def isborrow(self,borrow):
        if  isinstance(borrow,bool):
            self.__borrow = borrow
        else:
            raise ValueError("BORROW must be str")

class Library:
    def __init__(self,books_db):
        self.library_list = []
        self.books_db = books_db

    def read(self,id):
        if (len(book_list)==0):
            print("Empty")
        for index in range(len(self.books_db)):
            if ((index+1) == id):
                return self.books_db[index]
            


b1=Book("Development","Microsoft",False)
b2=Book("Cloud","Amazon",True)
b3=Book("Chip","Taiwan")
book_list = []
book_list.append(b1)
book_list.append(b2)
book_list.append(b3)

for one_book in book_list:
    print(one_book.title, " - ", one_book.author," - ",one_book.isborrow,end="\n")

print("<<CRUD>>")
b1crud=Library(book_list)
print(b1crud.read(1))
