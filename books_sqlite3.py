import sqlite3
from sys import path

class PrimaryKeyError(Exception):
    pass
database=sqlite3.connect(path[0]+"/books_db.db",check_same_thread=False)
cursor=database.cursor()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS books_table(isbn INTEGER PRIMARY KEY,title TEXT,author TEXT,price FLOAT,pages INTEGER)")
def insert_book(isbn,title,author,price,pages):
    try:
        cursor.execute("INSERT INTO books_table VALUES(?,?,?,?,?)",(isbn,title,author,price,pages))
        database.commit()
    except(sqlite3.IntegrityError):
        print("isbn must be a unique number")
def find_book(isbn):
  cursor.execute("SELECT * FROM books_table WHERE isbn=?",[isbn])
  data=cursor.fetchone()
  return data
def delete_book(isbn):
    cursor.execute("DELETE FROM books_table WHERE isbn=?",[isbn])
    database.commit()
def allbooks():
    return list(cursor.execute("SELECT * FROM books_table"))