from tensorflow.keras.preprocessing.image import img_to_array

def preprocess_image(image):
    image = image.resize((64, 64))
    image = img_to_array(image) / 255.0
    return image
