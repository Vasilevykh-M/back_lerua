from fastapi import FastAPI

from generator import Generator
from server import GenerateApi

app = FastAPI()
func = lambda x, y, z: x
g = Generator(func)

hello = GenerateApi(g)
app.include_router(hello.router)