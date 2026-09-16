from fastapi import FastAPI, HTTPException
from app.schemas.livro import LivroSchema
from app.routers import livros
from app.database.connection import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(livros.router)

# Rota inicial da API
@app.get("/")
async def home():
    return {"message": "Bem-vindo à API de Livros!"}