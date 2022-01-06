from sqlalchemy.sql.operators import isnot
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

    def saveTodo(self, todo_schema):
        todo = TodoModel(todo_schema.title, todo_schema.description)
        db = SessionLocal()
        db.add(todo)
        db.commit()
        db.refresh(todo) 
        db.close()
        return todo

    def deleteTodoById(self, todo_id):
        todo = self.getTodosById(todo_id)
        if todo is not None:
            db = SessionLocal()
            db.delete(todo)
            db.commit()
            db.close()
            return True
        return False
