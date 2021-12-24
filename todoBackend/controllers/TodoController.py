from fastapi import APIRouter

from ..services.TodoService import TodoService

router = APIRouter(prefix='/todo')

service = TodoService()

@router.get("/")
async def getAllTodos():
    return service.getAllTodos()
