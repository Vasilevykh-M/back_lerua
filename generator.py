from bacrkround_remover import RemoverKand
from clip_ import ClipModel
from model import InpaintingModel


class Generator:
  def __init__(self):
    self.clip = ClipModel()
    self.remover = RemoverKand()
    self.inpainting = InpaintingModel()
  def __call__(self, image):
    class_im = self.clip(image)
    mask, image = self.remover.remove_backgroud(image, class_im)
    return self.inpainting(image, mask, class_im)