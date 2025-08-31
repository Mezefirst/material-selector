from pydantic import BaseModel

class MaterialBase(BaseModel):
    name: str
    type: str
    color: str
    strength: float
    cost: float
    sustainability: float
    description: str = ""

class MaterialCreate(MaterialBase):
    pass

class MaterialOut(MaterialBase):
    id: int

    class Config:
        orm_mode = True
