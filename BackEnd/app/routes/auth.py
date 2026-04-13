from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.user import User
from app.core.hash import verify_password
from app.core.security import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(status_code=401, detail="Usuario no existe")

        if not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        token = create_token({"sub": user.email, "role": user.role})

        return {"access_token": token, "token_type": "bearer"}

    except Exception as e:
        print("🔥 ERROR EN LOGIN:", str(e))
        raise