from pydantic import BaseModel
from typing import List


class INFO(BaseModel):
    id: str
    x1: int


class Input(BaseModel):
    id: str
    score: int
    attr: List[INFO]

class Output(BaseModel):
    predict: str