import numpy as np
from tensorflow.keras.models import load_model
from detector.preprocess import preprocess_image

model = load_model("detector/model.h5")

def predict_lung_cancer(image):
    image = preprocess_image(image)
    prediction = model.predict(np.expand_dims(image, axis=0))[0][0]
    return "Cancerous" if prediction > 0.5 else "Non-Cancerous"
