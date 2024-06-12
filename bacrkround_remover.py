from PIL import Image, ImageOps
import requests
from io import BytesIO
from transparent_background import Remover
import torch

class RemoverKand():
  def __init__(self):
    self.remover = Remover(mode='base')
  def resize_with_padding(self, img, expected_size):
      img.thumbnail((expected_size[0], expected_size[1]))
      delta_width = expected_size[0] - img.size[0]
      delta_height = expected_size[1] - img.size[1]
      pad_width = delta_width // 2
      pad_height = delta_height // 2
      padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
      return ImageOps.expand(img, padding)

  def remove_backgroud(self, img):
    img = self.resize_with_padding(img, (512, 512))
    return self.remover.process(img, type='map'), img