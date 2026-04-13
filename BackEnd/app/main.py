from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import auth, remesa

from app.models.user import User
from app.models.transaction import Transaction

from fastapi.middleware.cors import CORSMiddleware

# 1. Crear la app PRIMERO
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en desarrollo está bien
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Incluir routers
app.include_router(auth.router)
app.include_router(remesa.router)

# 3. Crear tablas
Base.metadata.create_all(bind=engine)

# 4. Endpoint de prueba
@app.get("/")
def root():
    return {"message": "API funcionando"}