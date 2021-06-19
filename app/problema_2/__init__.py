from pydantic import BaseModel


class Transporte(BaseModel):
    largura: float
    altura: float
    espessura: float
    peso: float
