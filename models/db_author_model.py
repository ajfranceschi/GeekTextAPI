from core import app, db, marshmallow


# Authors table Model
class Authors(db.Model):
    __tablename__ = 'Authors'
    idAuthors = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    authorFirstName = db.Column(db.String(45) , nullable=False)
    authorLastName = db.Column(db.String(150), nullable=False)
    authorPublisher = db.Column(db.String(255))
    authorBiography = db.Column(db.Text)


# JSON Schema
class AuthorSchema(marshmallow.Schema):
    class Meta:
        fields = ('idAuthors', 'authorFirstName', 'authorLastName', 'authorPublisher', 'authorBiography')


Author_schema = AuthorSchema()
Authors_schema = AuthorSchema(many=True)

if __name__ == "__main__":
    db.create_all()
