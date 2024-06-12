class Generator:
  def __init__(self, model):
    self.model = model
  def __call__(self, image, text):
    return self.model(image, text)