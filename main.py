from fastapi import FastAPI
import numpy as np

from generator import Generator
from server import GenerateApi

app = FastAPI()
g = Generator(lambda x: np.zeros(3))

hello = GenerateApi(g)
app.include_router(hello.router)