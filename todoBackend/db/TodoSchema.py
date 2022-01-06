from pydantic import BaseModel
from typing import Optional

# TO support creation and update APIs
class TodoSchema(BaseModel):
    
    id: Optional[int] = None
    title: str
    description: str

    class Config:
        orm_mode = True

