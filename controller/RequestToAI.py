from pydantic import BaseModel

class RequestToAI(BaseModel):
    text : str
    role : str | None = None