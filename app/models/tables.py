from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    about = db.Column(db.Text(300), nullable=True)
    email = db.Column(db.String, unique=True)

    @property
    def is_authenticated(self):
        return True
        
    @property
    def is_active(self):
        return True
        
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, about, email):

        self.username = username
        self.password = password
        self.name = name
        self.about = about
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'


class Request(db.Model):

    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    about = db.Column(db.String(310))
    requisition = db.Column(db.String)

    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, about, requisition, user_id):
        self.about = about
        self.requisition = requisition
        self.user_id = user_id
