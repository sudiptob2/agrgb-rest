import numpy as np
from keras.models import load_model
from keras.preprocessing import image


class Detect:
    def __init__(self):
        self.classes = ["powdery mildew", "yellow mosaic"]
        self.model = load_model('model_mungbean.h5')
        self.image_size = 150

    def predict(self, img):
        img = np.expand_dims(img, axis=0)
        result = self.model.predict_classes(img)
        print(self.classes[result[0]])
