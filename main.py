from fastapi import FastAPI, File, UploadFile, APIRouter
import io
import numpy as np
from PIL import Image, ImageOps

class Generator:
  def __init__(self, model):
    self.model = model
  def generate(self, image):
    return self.model(image)

class GenerateApi:
  def __init__(self, generator):
    self.generator = generator
    self.router = APIRouter()
    self.router.add_api_route("/generate_background", self.generate_background, methods=["GET"])

  def generate_background(self, img_file:UploadFile = File(...)):

      if '.jpg' in img_file.filename or '.jpeg' in img_file.filename or '.png' in img_file.filename:

          request_object_content = img_file.read()
          img = Image.open(io.BytesIO(request_object_content))
          result = self.generator.generate(img)
          return result.tobytes()

app = FastAPI()
g = Generator(lambda x: np.zeros(3))

hello = GenerateApi(g)
app.include_router(hello.router)