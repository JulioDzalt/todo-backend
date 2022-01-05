from pydantic import BaseModel

# TO support creation and update APIs
class TodoSchema(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True

