from fastapi import FastAPI, HTTPException

# Lista de livros inicial
Livros = ["Lupin", "Odisseia", "O Hobbit", "A Guerra dos Tronos"]

app = FastAPI()

# Rota inicial da API
@app.get("/")
async def home():
    return {"message": "Bem-vindo à API de Livros!"}

# Lista todos os livros
@app.get("/livros")
async def listar_livros():
    return {"livros": Livros}

# Adiciona um novo livro
@app.post("/livros")
async def adicionar_livro(livro: str):
    Livros.append(livro)
    return {"message": "Livro adicionado com sucesso!"}

# Atualiza um livro existente
@app.put("/livros/{index}")
async def atualizar_livro(index: int, new_livro: str):
    if index >= len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    Livros[index] = new_livro
    return {"message": "Livro atualizado com sucesso!"}

# Remove um livro existente
@app.delete("/livros/{index}")
async def remover_livro(index: int):
    if index >= len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    Livros.pop(index)
    return {"message": "Livro removido com sucesso!"}