from typing_extensions import Concatenate
import yaml
from fastapi import FastAPI

config = "It's works"

with open(r'/home/julio/Desktop/todo-backend/config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": config["defaultMessage"]}
