from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model = load_model('poultry_model.h5')

# Replace these class names with your actual dataset labels
classes = ['Healthy', 'Coccidiosis', 'Newcastle', 'Infectious Bronchitis']

# Image size used during training (adjust if needed)
IMG_SIZE = (224, 224)

def predict_disease(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img) / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]

    return predicted_class

