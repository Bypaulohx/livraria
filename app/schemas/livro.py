from pydantic import BaseModel, ConfigDict, Field


class LivroBase(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    autor: str = Field(min_length=3, max_length=100)
    ano_publicacao: int = Field(ge=0, description="Ano de publicação do livro")


class LivroCreate(LivroBase):
    pass


class LivroSchema(LivroBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class LivroResponse(LivroSchema):
    pass