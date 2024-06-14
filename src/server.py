import cv2
import numpy as np
from PIL import Image
from fastapi import File, UploadFile, APIRouter, HTTPException, status
from fastapi.responses import PlainTextResponse
from io import BytesIO
import base64


def load_image_into_numpy_array(data):
    npimg = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    return frame

def image2base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

class GenerateApi:
    def __init__(self, generator):
        self.generator = generator
        self.router = APIRouter()
        self.router.add_api_route(
            "/generate_background", self.generate_background, methods=["POST"])

    async def generate_background(self, img_file: UploadFile = File(...)):
        if all(ext not in img_file.filename for ext in ['.jpg', '.jpeg', '.png']):
            return HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail=f'File {img_file.filename} has unsupported extension type',
            )
        img = load_image_into_numpy_array(await img_file.read())
        result_img = self.generator(img)
        return PlainTextResponse(image2base64(result_img))