from clip_model import ClipModel
from image_preprocessor import ImagePreprocessor
from inpainting_model import InpaintingModel
from config import templates


class Generator:
    def __init__(self):
        self.clip = ClipModel(templates)
        self.preprocessor = ImagePreprocessor()
        self.inpainting = InpaintingModel()

    def __call__(self, image):
        class_im = self.clip(image)
        print(class_im)
        image, mask = self.preprocessor(image, class_im['scale'], class_im['y_pos'])
        return self.inpainting(image, mask, class_im)
