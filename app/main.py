from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import auth, remesa

from app.models.user import User
from app.models.transaction import Transaction

# 1. Crear la app PRIMERO
app = FastAPI()

# 2. Incluir routers
app.include_router(auth.router)
app.include_router(remesa.router)

# 3. Crear tablas
Base.metadata.create_all(bind=engine)

# 4. Endpoint de prueba
@app.get("/")
def root():
    return {"message": "API funcionando"}