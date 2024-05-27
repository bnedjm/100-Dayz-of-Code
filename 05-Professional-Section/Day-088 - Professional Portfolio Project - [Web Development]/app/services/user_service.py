from app.models import User, Cafe
from app import db

def create_user(username, email): # TBD
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user
