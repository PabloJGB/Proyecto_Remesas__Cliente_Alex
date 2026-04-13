from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models import Transaction
from app.services.exchange import get_usd_to_gtq_rate

router = APIRouter(prefix="/remesa", tags=["Remesas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 💸 Enviar dinero (HIJO)
@router.post("/send")
def send_money(sender_id: int, receiver_id: int, amount_usd: float, db: Session = Depends(get_db)):
    
    rate = get_usd_to_gtq_rate()
    amount_gtq = amount_usd * rate

    transaction = Transaction(
        sender_id=sender_id,
        receiver_id=receiver_id,
        amount_usd=amount_usd,
        amount_gtq=amount_gtq,
        rate=rate
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


# 🙋 Solicitud de dinero (RECEPTOR)
@router.post("/request")
def request_money(sender_id: int, receiver_id: int, amount_gtq: float, db: Session = Depends(get_db)):
    
    rate = get_usd_to_gtq_rate()
    amount_usd = amount_gtq / rate

    transaction = Transaction(
        sender_id=sender_id,
        receiver_id=receiver_id,
        amount_usd=amount_usd,
        amount_gtq=amount_gtq,
        rate=rate
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


# 📄 Listado con paginación
@router.get("/")
def get_transactions(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    
    offset = (page - 1) * limit

    transactions = db.query(Transaction).offset(offset).limit(limit).all()

    return transactions