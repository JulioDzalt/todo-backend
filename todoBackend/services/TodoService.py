from ..models.TodoModel import TodoModel
from fastapi import Depends
from typing import List
from sqlalchemy.orm import Session

from ..db.db import SessionLocal

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


    def getAllTodos(self, db: Session = Depends(get_db)) -> List[TodoModel]:
        # lstTodos = [TodoModel("1","1"), TodoModel("2","2"),]
        # return {"data": lstTodos}

        todos = db.query(TodoModel).all()
        return todos
