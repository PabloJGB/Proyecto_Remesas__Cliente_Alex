from app.db.database import SessionLocal
from app.models.user import User
from app.core.hash import hash_password

db = SessionLocal()

user1 = User(
    email="test1@mail.com",
    password=hash_password("123"),
    role="HIJO"
)

user2 = User(
    email="test2@mail.com",
    password=hash_password("123"),
    role="RECEPTOR"
)

db.add(user1)
db.add(user2)
db.commit()

print("Usuarios creados correctamente")