from fastapi import FastAPI
import numpy as np

from generator import Generator
from server import GenerateApi

app = FastAPI()
func = lambda x, y: x+1
g = Generator(func)

hello = GenerateApi(g)
app.include_router(hello.router)