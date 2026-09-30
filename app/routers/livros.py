from fastapi import APIRouter, HTTPException
from app.schemas.livro import LivroSchema
from app.database.connection import SessionLocal
from app.database.models import LivroModel
from app.schemas.livro import LivroCreate
from app.database.connection import get_db
from app.services import livro_service

router = APIRouter(
    prefix="/livros",
    tags=["livros"],
)

# Lista todos os livros
@router.get("/")
async def listar_livros(
    db:Session = Depends(get_db)
):
    return livro_service.listar_livros(db)

# Adiciona um novo livro
@router.post("/")
async def adicionar_livro(
    livro: LivroCreate,
    db: Session = Depends(get_db)):

    return livro_service.adicionar_livro(livro, db)

# Atualiza um livro existente
@router.put("/{index}")
async def atualizar_livro(
    index: int,
    livro: LivroCreate,
    db: Session = Depends(get_db)
    ):

    livro_db = livro_service.atualizar_livro(index, livro, db)

    if not livro_db:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")

    return livro_db

# Remove um livro existente
@router.delete("/{index}")
async def remover_livro(
    index: int,
    db: Session = Depends(get_db)
    ):

    removido = livro_service.remover_livro(index, db)
    db.close()

    if not removido:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")

    return {"message": "Livro removido com sucesso!"}