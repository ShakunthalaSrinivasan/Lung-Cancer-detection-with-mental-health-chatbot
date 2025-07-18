import numpy as np
from tensorflow.keras.models import load_model
from detector.preprocess import preprocess_image

# Load the model once
model = load_model("detector/model.h5")

def predict_lung_cancer(image):
    try:
        # Preprocess the image
        image = preprocess_image(image)

        # Predict
        prediction = model.predict(np.expand_dims(image, axis=0))[0][0]

        # Return result
        return "Cancerous" if prediction > 0.5 else "Non-Cancerous"
    
    except Exception as e:
        print(f"Prediction error: {e}")
        return "Prediction Failed"
