from fastapi import FastAPI

from generator import Generator
from server import GenerateApi

app = FastAPI()
g = Generator()

hello = GenerateApi(g)
app.include_router(hello.router)