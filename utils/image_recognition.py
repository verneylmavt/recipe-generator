# utils/image_recognition.py
import tensorflow as tf
import numpy as np
from PIL import Image

class ImageRecognizer:
    def __init__(self):
        self.model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=True)
        self.preprocess = tf.keras.applications.mobilenet_v2.preprocess_input
        self.decode = tf.keras.applications.mobilenet_v2.decode_predictions
    
    def recognize_image(self, image_path):
        try:
            img = Image.open(image_path).resize((224, 224))
            img_array = np.array(img)
            if img_array.shape[-1] == 4:
                img_array = img_array[..., :3]
            img_array = np.expand_dims(img_array, axis=0)
            img_array = self.preprocess(img_array)
            predictions = self.model.predict(img_array)
            decoded = self.decode(predictions, top=5)[0]
            ingredients = [self.map_label_to_ingredient(item[1]) for item in decoded]
            ingredients = list(set([ing for ing in ingredients if ing]))
            return ingredients
        except Exception as e:
            print(f"Error in image recognition: {e}")
            return []
    
    def map_label_to_ingredient(self, label):
        label_mapping = {
            'chicken': 'chicken',
            'broccoli': 'broccoli',
            'rice': 'rice',
            'tomato': 'tomato',
            'carrot': 'carrot',
            'lettuce': 'lettuce',
            'apple': 'apple',
            'banana': 'banana',
            'cheeseburger': 'beef',
            'pizza': 'cheese',
            'butter': 'butter',
            'egg': 'egg',
            'flour': 'flour',
            'sugar': 'sugar',
            'milk': 'milk',
            'oil': 'vegetable oil',
            'garlic': 'garlic',
            'onion': 'onion',
            'pepper': 'pepper',
            'salt': 'salt',
            'spinach': 'spinach',
            'mushroom': 'mushroom',
            'fish': 'fish',
            'shrimp': 'shrimp',
            'pasta': 'pasta',
            'beans': 'beans',
            'peas': 'peas',
            'cheese': 'cheese',
            'olive': 'olive',
            'lettuce': 'lettuce',
            'soup': 'soup',
            'steak': 'steak',
            'cucumber': 'cucumber',
            'orange': 'orange',
            'lemon': 'lemon',
            'strawberry': 'strawberry',
            'banana': 'banana',
        }
        return label_mapping.get(label.lower(), None)