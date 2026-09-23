from pydantic import BaseModel, Field, ConfigDict

class LivroSchema(BaseModel):
    id: int
    titulo: str = Field(min_length=3, max_length=100)
    autor: str = Field(min_length=3, max_length=100)
    ano_publicacao: int = Field(ge=0, description="Ano de publicação do livro")

class LivroCreate(LivroSchema):
    pass

class LivroResponse(LivroSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)