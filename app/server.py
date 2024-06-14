import cv2
import numpy as np
from PIL import Image
from fastapi import File, UploadFile, APIRouter, HTTPException, status
from fastapi.responses import PlainTextResponse
from io import BytesIO
import base64


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
        request_object_content = await img_file.read()
        img = Image.open(BytesIO(request_object_content))
        result_img = self.generator(img)
        return PlainTextResponse(image2base64(result_img))
