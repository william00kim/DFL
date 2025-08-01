from pydantic import BaseModel
from enum import Enum

class RequestToAI(BaseModel):
    model: str
    prompt : str
    role : str | None = None

class Model(str, Enum):
    gemma = "gemma"
    exaone = "exaone"