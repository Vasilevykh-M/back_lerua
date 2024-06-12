from PIL import Image
import numpy as np
from bacrkround_remover import RemoverKand
from clip import ClipModel


class Generator:
  def __init__(self, model):
    self.model = model
    self.clip = ClipModel()
    self.remover = RemoverKand()
  def __call__(self, image):
    class_im, type_im = self.clip(image)
    mask, image = self.remover.remove_backgroud(image, type_im)
    image = image * (np.array(mask) / 255)
    return self.model(Image.fromarray(image.astype(np.uint8)), class_im)