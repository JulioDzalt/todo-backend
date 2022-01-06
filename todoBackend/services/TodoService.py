from fastapi import HTTPException
from ..db.db import SessionLocal, engine
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
        todo = TodoModel()
        todo.title = todo_schema.title
        todo.description = todo_schema.description
        db = SessionLocal()
        db.add(todo)
        db.commit()
        db.refresh(todo) 
        db.close()
        return todo
        
    def updateTodo(self, todo_schema):
        
        db = SessionLocal()
        todo = None
        if todo_schema.id is not None:
            todo = db.query(TodoModel).filter_by(id=todo_schema.id).first()
            if todo is not None:
                todo.title = todo_schema.title
                todo.description = todo_schema.description
                db.commit()
                db.refresh(todo) 
        db.close()
        
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        
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
