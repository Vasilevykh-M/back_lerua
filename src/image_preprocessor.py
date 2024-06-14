from PIL import ImageOps, Image
from transparent_background import Remover


class ImagePreprocessor():
    def __init__(self):
        self.remover = Remover(mode='base')

    def resize_with_padding(self, img, type_img):
        max_size = max(img.size[1], img.size[0])
        border_h = (max_size - img.size[1]) // 2
        border_w = (max_size - img.size[0]) // 2

        scale = type_img["scale"]
        border_pad = type_img["padding"]

        border_h += int((1 - scale) * max_size)
        border_w += int((1 - scale) * max_size)

        return ImageOps.expand(img, border=(
            border_w,
            border_h - (int)(border_pad * border_h),
            border_w,
            border_h + (int)(border_pad * border_h)))

    def remove_backgroud(self, img, type_img):
        img = self.resize_with_padding(img, type_img)
        img = img.resize((640, 640), Image.Resampling.LANCZOS)
        mask = self.remover.process(img, type='map')
        mask = ImageOps.invert(mask)
        return mask, img