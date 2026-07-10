import books_sqlite3 as sql
class Book:
    """
    A class to represent a book.
    """
    count = 0

    def __init__(self, isbn, title, author, price, pages) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self._exists = True
        sql.insert_book(self.isbn, self.title, self.author, self.price, self.pages)

    @property
    def isbn(self):
        return self._i
    @isbn.setter
    def isbn(self,value):
        if isinstance(value,int):
            self._i=value
        else:
            raise ValueError("isbn Must be a 8-digit number!")
    @property
    def price(self):
        return self._p
    @price.setter
    def price(self,value):
        if  value>0 and isinstance(value,float):
            self._p=value
        else:
            raise ValueError("Price must be a number!")
    @staticmethod
    def findbook(isbn) :
        return sql.find_book(isbn)
    @staticmethod
    def delete(isbn):
        return sql.delete_book(isbn)
    @staticmethod
    def allbooks():
        return sql.allbooks()
#--------------------Main-----------------------

    