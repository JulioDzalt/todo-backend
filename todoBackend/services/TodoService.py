from ..db.db import SessionLocal, engine
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..models import TodoModel as TodoModelFile
from ..models.TodoModel import TodoModel

TodoModelFile.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()

class TodoService:

    # def __init__(self, id): #Constructor
    #     self.id = id

    def getAllTodos(self, db = get_db()):
        todos = db.query(TodoModel).all()
        return todos

    def getTodosById(self, todo_id, db = get_db()):
        todos = db.query(TodoModel).get(todo_id)    
        return todos