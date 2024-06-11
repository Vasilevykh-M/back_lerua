class Generator:
  def __init__(self, model):
    self.model = model
  def generate(self, image):
    return self.model(image)