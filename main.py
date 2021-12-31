import os
import yaml
from fastapi import FastAPI
from todoBackend.controllers import TodoController

cwd = os.getcwd()
config_file_path = cwd+'/config.yml'
file = open(config_file_path, "r")
config = yaml.load(file, Loader=yaml.FullLoader)


app = FastAPI()
app.include_router(TodoController.router)

@app.get("/")
async def root():
    return {"message": config["defaultMessage"]}

@app.get("/version/")
async def root():
    return {"version": config["version"]}
