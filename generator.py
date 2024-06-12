from PIL import Image
import numpy as np
from bacrkround_remover import RemoverKand
from clip_ import ClipModel


class Generator:
  def __init__(self, model):
    self.model = model
    self.clip = ClipModel()
    self.remover = RemoverKand()
  def __call__(self, image):
    class_im, type_im = self.clip(image)
    mask, image = self.remover.remove_backgroud(image, type_im)
    return self.model(image, mask, class_im)