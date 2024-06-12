from PIL import Image, ImageOps
import requests
from io import BytesIO
from transparent_background import Remover
import torch

class RemoverKand():
  def __init__(self):
    self.remover = Remover(mode='base')
  def resize_with_padding(self, img, type_img):
      new_w = img.size[0] * 2
      new_h = img.size[1] * 2
      border_h = img.size[1]
      border_w = img.size[0]
      img.thumbnail((new_w, new_h))
      border_pad = 0
      if type_img == 1:
          border_pad = 0.75
      if type_img == 2:
          border_pad = 0.5
      if type_img == 3:
          border_pad = 0

      return ImageOps.expand(img, border=(
          border_w,
          border_h - (int)(border_pad * border_h),
          border_w,
          border_h + (int)(border_pad * border_h)
      ), fill=(0, 0, 0, 0))

  def remove_backgroud(self, img, type_img):
    img = self.resize_with_padding(img, type_img)
    return self.remover.process(img, type='map'), img