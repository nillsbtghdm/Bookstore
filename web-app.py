from book_app import Book
from books_sqlite3 import PrimaryKeyError

import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/newbook", methods=["POST", "GET"])
def newbook():
    if flask.request.method == "POST":
        book_data = dict(flask.request.form)
        try:
            Book(int(book_data["isbn"]), book_data["title"], book_data["author"],
                 float(book_data["price"]), int(book_data["pages"]))
        except PrimaryKeyError:
            return flask.render_template("error.html", message="Primary Key Error: This ISBN already exists.")
        except ValueError:
            return flask.render_template("error.html", message="Value Error: Please enter correct data")
        return flask.redirect("/")
    return flask.render_template("newbook.html") 

@app.route("/bookslist")
def bookslist():
    all = Book.allbooks()
    return flask.render_template("bookslist.html",allbooks=all)

@app.route("/deletebook", methods=["GET","POST"])
def deletebook():
    if flask.request.method == "POST" :
        isbn = dict(flask.request.form)
        Book.delete(isbn["isbn"])
        return flask.redirect("/bookslist")        
    return flask.render_template("deletebook.html")
@app.route("/findbook.html", methods=["GET", "POST"])
def findbook():
    if flask.request.method == "POST":
        book_isbn = dict(flask.request.form)
        book=Book.findbook(book_isbn["isbn"])
        return flask.render_template("findbook.html",book=book)
    return flask.render_template("findbook.html")

app.run(debug=True)