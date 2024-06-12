import clip
import torch


class ClipModel:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)

        self.data_label = ['chandeliers for lamps (interior)',
                      'LED chandeliers (interior)',
                      'street lamp under a lamp',
                      'LED street lamp',
                      'street lamp posts (exterior)',
                      'LED panel (interior)',
                      'night light (interior inside the house)',
                      'table lamps under a lamp (interior)',
                      'LED table lamps',
                      'Garden furniture',
                      'B-B-Q']
        self.text = clip.tokenize(self.data_label).to(self.device)

    def __call__(self, image):
        image = self.preprocess(image).unsqueeze(0).to(self.device)
        logits_per_image, logits_per_text = self.model(image, self.text)
        idx = torch.argmax(logits_per_image.softmax(dim=-1)).item()
        probs = self.data_label[idx]
        img_group = 0
        if idx == 0 or idx == 1 or idx == 5:
            img_group = 0
        if idx == 2 or idx == 3 or idx == 4:
            img_group = 1
        if idx == 6 or idx == 7 or idx == 8 or idx == 9 or idx == 10:
            img_group = 2
        return probs, img_group

