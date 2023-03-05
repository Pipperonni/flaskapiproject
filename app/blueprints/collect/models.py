from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    collect = db.relationship('CollectedPokemon', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"<User: {self.username}>"
    def __str__(self):
        return f'User: {self.email}|{self.username}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class CollectedPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon = db.Column(db.String(40))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
