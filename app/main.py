from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Ainmensaginha"}

@app.get("/saudacao")
async def saudacao(string: str):
    return {"message": f"Olá, {string}! Seja bem-vindo!"}