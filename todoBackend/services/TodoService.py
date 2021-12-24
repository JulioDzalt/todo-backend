from ..models.TodoModel import TodoModel

class TodoService:

    # def __init__(self, id): #Constructor
    #     self.id = id

    def getAllTodos(self):
        lstTodos = [TodoModel("1","1"), TodoModel("2","2"),]
        return {"data": lstTodos}
