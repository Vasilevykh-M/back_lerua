import clip
import torch


class ClipModel:
    
    def __init__(self, data_label):
        # self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)

        self.data_label = data_label
        self.text = clip.tokenize([i["value"] for i in self.data_label]).to(self.device)


    def __call__(self, image):
        image = self.preprocess(image).unsqueeze(0).to(self.device)
        logits_per_image, logits_per_text = self.model(image, self.text)
        idx = torch.argmax(logits_per_image.softmax(dim=-1)).item()
        return self.data_label[idx]

