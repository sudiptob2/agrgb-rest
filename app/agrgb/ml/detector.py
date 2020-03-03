import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import cv2
from tensorflow.keras.models import load_model
import numpy as np


class Detect:
    def __init__(self):
        self.classes = ["powdery mildew", "yellow mosaic"]
        self.model = load_model("model_mug.h5")
        print("Model loaded")
        self.image_size = 150

    def predict(self, img):
        print("Starting predict")
        img = cv2.resize(img, (150, 150))
        img = np.expand_dims(img, axis=0)
        result = self.model.predict_classes(img)
        value = self.classes[result[0]]
        print(value)
        return value
