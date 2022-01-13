# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Raavan', 'Amish Tripathi', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# new_book = Book(id=1, title="Raavan", author="Amish Tripathi", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


# CREATE
# new_book1 = Book(title="Ram", author="Amish Tripathi", rating=10.0)
# db.session.add(new_book1)
# db.session.commit()


# READ
all_books = db.session.query(Book).all()
print(all_books)

book = Book.query.filter_by(title="Ram").first()
print(book)


# UPDATE
# book_to_update = Book.query.filter_by(title="Raavan").first()
# book_to_update.title = "Sita"
# db.session.commit()

# new_book = Book(title="Raavan", author="Amish Tripathi", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

book_id = 3
book_to_update = Book.query.filter_by(id=book_id).first()
book_to_update.title = "Shiva"
db.session.commit()

# DELETE

book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()


