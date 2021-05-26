
from app import db
from database import User

def create_my_user(first_name, last_name, hobbies):
  db.session.add(
    User(
      first_name=first_name,
      last_name=last_name,
      hobbies=hobbies
    )
  )
  db.session.commit()

if __name__ == "__main__":
  create_my_user("Jerald", "Mac", "Jiu Jitsu")
  users = User.query.all()
  print(users)
  create_my_user("John", "Doe", "Minning for diamonds")
  user = User.query.filter_by(first_name="John").first()
  print(user)