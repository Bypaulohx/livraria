from fastapi import APIRouter, HTTPException
from app.schemas.livro import LivroSchema

router = APIRouter(
    prefix="/livros",
    tags=["livros"],
)

Livros = [
    LivroSchema(id=1, titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", ano_publicacao=1954),
    LivroSchema(id=2, titulo="1984", autor="George Orwell", ano_publicacao=1949),
    LivroSchema(id=3, titulo="O Pequeno Príncipe", autor="Antoine de Saint-Exupéry", ano_publicacao=1943),
    LivroSchema(id=4, titulo="Dom Casmurro", autor="Machado de Assis", ano_publicacao=1899),
]

# Lista todos os livros
@router.get("/")
async def listar_livros():
    return {"livros": Livros}

# Adiciona um novo livro
@router.post("/")
async def adicionar_livro(livro: LivroSchema):
    Livros.append(livro)
    return {"message": "Livro adicionado com sucesso!"}

# Atualiza um livro existente
@router.put("/{index}")
async def atualizar_livro(index: int, livro: LivroSchema):
    if index >= len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    Livros[index] = livro
    return {"message": "Livro atualizado com sucesso!"}

# Remove um livro existente
@router.delete("/{index}")
async def remover_livro(index: int):
    if index >= len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    Livros.pop(index)
    return {"message": "Livro removido com sucesso!"}