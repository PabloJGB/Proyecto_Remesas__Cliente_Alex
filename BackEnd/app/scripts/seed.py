from app.db.database import SessionLocal
from app.models.user import User
from app.core.hash import hash_password

def seed():
    db = SessionLocal()

    # evitar duplicados
    if db.query(User).first():
        print("Usuarios ya existen, no se ejecuta seed")
        return

    users = [
        User(
            email="hijo@mail.com",
            password=hash_password("123"),
            role="HIJO"
        ),
        User(
            email="alex@mail.com",
            password=hash_password("123"),
            role="RECEPTOR"
        )
    ]

    db.add_all(users)
    db.commit()
    db.close()

    print("Usuarios creados correctamente")

if __name__ == "__main__":
    seed()