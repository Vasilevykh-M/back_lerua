import cv2
import numpy as np
from PIL import Image
from fastapi import File, UploadFile, APIRouter, HTTPException, status


def load_image_into_numpy_array(data):
    npimg = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    return frame

class GenerateApi:
  def __init__(self, generator):
    self.generator = generator
    self.router = APIRouter()
    self.router.add_api_route("/generate_background", self.generate_background, methods=["POST"])

  async def generate_background(self, img_file:UploadFile = File(...)):

      if '.jpg' in img_file.filename or '.jpeg' in img_file.filename or '.png' in img_file.filename:

          img = load_image_into_numpy_array(await img_file.read())
          result = self.generator(img)
          return str(result.tobytes())
      return  HTTPException(
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        detail=f'File {img_file.filename} has unsupported extension type',
    )