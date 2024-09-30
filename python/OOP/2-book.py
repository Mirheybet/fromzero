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
    def __str__(self):
        borrow_status = "Borrow" if self.isborrow else "Available"
        return f'{self.title} by {self.author} ({borrow_status})'

class Library:
    def __init__(self,books_db):
        self.library_list = []
        self.books_db = books_db

    def read(self,id):
        if (len(book_list)==0):
            print("Empty")
        for index in range(len(self.books_db)):
            if (index == (id-1)):
                return self.books_db[index]

    def create(self,title,author,isborrow):
        new_book = Book(title,author,isborrow)
        self.books_db.append(new_book)
        print("Book successful added....",end="\n")
        print(f"Book '{new_book.title}' by {new_book.author} has been added to the library.\n")
        print(f"Book status is {new_book.isborrow}!")

    def update(self,n_nth_book,n_title,n_author,n_isborrow):
        if(isinstance(n_nth_book,int)):
            if (n_nth_book < 0 or n_nth_book > len(self.books_db)):
                raise IndexError(f"There are not {n_nth_book} ID book in library :(")
        
            book_upd = self.books_db[n_nth_book - 1]
        
            if n_title:
                book_upd.title = n_title
            if n_author:
                book_upd.author = n_author
            if n_isborrow:
                book_upd.isborrow = n_isborrow
        else:
            raise TypeError("Book id must be integer")
    def delete(self,id):
         if(isinstance(id,int)):
            if (id < 0 or id > len(self.books_db)):
                raise IndexError(f"There are not {n_nth_book} ID book in library :(")
            process = self.books_db.pop(id-1)

b1=Book("Development","Microsoft",False)
b2=Book("Cloud","Amazon",True)
b3=Book("Chip","Taiwan")
book_list = []
book_list.append(b1)
book_list.append(b2)
book_list.append(b3)

for id,one_book in enumerate(book_list,start=1):
    print(id,". ",one_book.title, " - ", one_book.author," - ",one_book.isborrow,end="\n")

print("\n<<CRUD starting....>>\n")
b1crud=Library(book_list)

#READ-for nth book
print("\n(C)Read(UD)")
print("(C)Read(UD) STARTING....")
nth_book_liblist = int(input("N-th book index,pls write:"))
print(f"\n{nth_book_liblist} -th book:\n")
print(b1crud.read(nth_book_liblist))
print("(C)Read(UD) COMPLETED!\n")

#Create
print("\nCreate(RUD) STARTING....")
title = input("Enter book title: ")
author = input("Enter book author: ")
isborrow = input("Is the book borrowed? (yes/no): ").lower() == "yes"
b1crud.create(title, author, isborrow)
print("After UPDATE")
for id,i in enumerate(book_list,start=1):
    print(f"{id}. {i}")
print("\nCreate(RUD) COMPLETED!\n")

#Update
print("\n(CR)Update(D) STARTING....\n")
upd_id = int(input("Enter book id(integer): "))
upd_title = input("Enter book title: ")
upd_author = input("Enter book author: ")
upd_isborrow = input("Is the book borrowed? (yes/no): ").lower() == "yes"
b1crud.update(upd_id,upd_title,upd_author,upd_isborrow)
print("After UPDATE")
for id,i in enumerate(book_list,start=1):
    print(f"{id}. {i}")
print("\n(CR)Update(D) COMPLETED....\n")

#Delete
print("\n(CRU)Delete STARTING....\n")
del_id = int(input("Enter book id(integer): "))
a_or_dagree = input("Do you agree (yes/no): ")
if (a_or_dagree.lower() == "yes"):
    b1crud.delete(del_id)
    print("After UPDATE")
    for id,i in enumerate(book_list,start=1):
        print(f"{id}. {i}")
    print("\n(CR)Update(D) COMPLETED....\n")
else:
    print("DELETE cancelled!")
    

print("\n<<CRUD completed....>>\n")
