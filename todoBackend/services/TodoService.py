from ..models.TodoModel import TodoModel
from fastapi import Depends
from typing import List
from sqlalchemy.orm import Session

from ..db.db import SessionLocal, engine

from ..models import TodoModel

TodoModel.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TodoService:

    # def __init__(self, id): #Constructor
    #     self.id = id


    def getAllTodos(db: Session = Depends(get_db)):
        # lstTodos = [TodoModel("1","1"), TodoModel("2","2"),]
        # return {"data": lstTodos}

        todos = db.query(TodoModel).all()
        return todos
