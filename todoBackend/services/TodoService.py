from ..db.db import SessionLocal, engine
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..models import TodoModel as TodoModelFile
from ..models.TodoModel import TodoModel

TodoModelFile.Base.metadata.create_all(bind=engine)

class TodoService:

    # def __init__(self, id): #Constructor
    #     self.id = id

    def getAllTodos(self):
        db = SessionLocal()
        todos = db.query(TodoModel).all()
        db.close()
        return todos

    def getTodosById(self, todo_id):
        db = SessionLocal()
        todos = db.query(TodoModel).get(todo_id)
        db.close() 
        return todos