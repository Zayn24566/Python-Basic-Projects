from models import db , User

def create_user(data):
    user= User(
        name=data["name"],
        email=data["email"]
    )
    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    return User.query.all()

def delete_user(id):
    user = User.query.get(id)
    if user: 
        db.session.delete(user)
        db.session.commit()
        return True
    return False

def update_user(id, data):
    user = User.query.get(id) 
    if user:
        user.name = data.get("name", user.name) 
        user.email = data.get("email", user.email) 
        db.session.commit() 
    return user


