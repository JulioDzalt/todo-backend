from fastapi import APIRouter
from typing import List
from ..db.TodoSchema import TodoSchema
from fastapi.params import Depends
from ..services.TodoService import TodoService
from ..db.db import SessionLocal, engine
from sqlalchemy.orm import Session

router = APIRouter(prefix='/todo')

service = TodoService()

from ..models import TodoModel as TodoModelFile
from ..models.TodoModel import TodoModel

TodoModelFile.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@router.get("/")
async def getAllTodos():
    return service.getAllTodos()

@router.get('/1',response_model=List[TodoSchema])
def show_users(db:Session=Depends(get_db)):
    usuarios = db.query(TodoModel).all()
    return usuarios
