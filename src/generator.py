from clip_model import ClipModel
from image_preprocessor import ImagePreprocessor
from inpainting_model import InpaintingModel
from config import templates


class Generator:
    def __init__(self):
        self.clip = ClipModel(templates)
        self.remover = ImagePreprocessor()
        self.inpainting = InpaintingModel()

    def __call__(self, image):
        class_im = self.clip(image)
        mask, image = self.remover.remove_backgroud(image, class_im)
        return self.inpainting(image, mask, class_im)
