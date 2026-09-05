from pydantic import BaseModel

class PlayerCreate(BaseModel):
    name: str
    score: int = 0
    is_alive: bool = True

class PlayerResponse(PlayerCreate):
    id: int

    class Config:
        from_attributes = True