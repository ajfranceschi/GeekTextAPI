# ===============================================================
# Created by: Antonio J. Franceschi & Carlos Gonzalez
#
# This file contains the database queries for GeekText API
# Author details
# ===============================================================
from core import app, db, marshmallow


# Authors table Model
class Authors(db.Model):
    __tablename__ = 'Authors'
    idAuthors = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    authorFirstName = db.Column(db.String(45), nullable = False)
    authorLastName = db.Column(db.String(150), nullable = False)
    authorPublisher = db.Column(db.String(255))
    authorBiography = db.Column(db.Text)

    # Create an author with first name, last name, biography and publisher
    def createAuthor(authorFirstName, authorLastName, authorPublisher, authorBiography):
        new_author = Authors(authorFirstName = authorFirstName, authorLastName = authorLastName,
                             authorPublisher = authorPublisher, authorBiography = authorBiography)
        db.session.add(new_author)
        db.session.commit()


# JSON Schema
class AuthorSchema(marshmallow.Schema):
    class Meta:
        fields = ('idAuthors', 'authorFirstName', 'authorLastName', 'authorPublisher', 'authorBiography')


Author_schema = AuthorSchema()
Authors_schema = AuthorSchema(many = True)

if __name__ == "__main__":
    db.create_all()
