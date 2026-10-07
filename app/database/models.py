from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class LivroModel(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(100), nullable=False)
    ano_publicacao = Column(Integer, nullable=False)