from sqlalchemy.orm import Session
from app.database.models import LivroModel
from app.schemas.livro import LivroCreate

def listar_livros(db: Session):
    return db.query(LivroModel).all()