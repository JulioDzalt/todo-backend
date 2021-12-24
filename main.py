from typing_extensions import Concatenate
import yaml
from fastapi import FastAPI
from todoBackend.controllers import TodoController

# config = "It's works"

# with open(r'/todo-backend/config.yml') as file:
#     config = yaml.load(file, Loader=yaml.FullLoader)


app = FastAPI()

app.include_router(TodoController.router)

@app.get("/")
async def root():
    return {"message": "defaultMessage"}

@app.get("/version/")
async def root():
    return {"version": "version"}
