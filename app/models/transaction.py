from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from datetime import datetime
from app.db.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))

    amount_usd = Column(Float)
    amount_gtq = Column(Float)
    rate = Column(Float)

    status = Column(String, default="PENDIENTE")  # PENDIENTE / COMPLETADO

    created_at = Column(DateTime, default=datetime.utcnow)