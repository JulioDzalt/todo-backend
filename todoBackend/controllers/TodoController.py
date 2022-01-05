from fastapi import APIRouter
from typing import List
from ..db.TodoSchema import TodoSchema
from ..services.TodoService import TodoService
from ..db.db import SessionLocal, engine

router = APIRouter(prefix='/todo')

service = TodoService()

@router.get("/", response_model=List[TodoSchema])
async def getAllTodos():
    return service.getAllTodos()

@router.get("/{todo_id}", response_model=TodoSchema)
async def getTodosById(todo_id:int):
    return service.getTodosById(todo_id)
    