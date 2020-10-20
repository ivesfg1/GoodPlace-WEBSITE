from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String)
    about = db.Column(db.Text(418), nullable=True)
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

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Request(db.Model):

    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    about = db.Column(db.String(418))
    requisition = db.Column(db.String, unique=True)

    user = db.relationship("User", foreign_keys=user_id)


class Help(db.Model):

    __tablename__ = 'helps'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"))

    user = db.relationship("User", foreign_keys=user_id)
    request = db.relationship("Request", foreign_keys=request_id)