import os
import numpy as np
from tensorflow.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from PIL import Image

input_path = "" #your input dataset
output_path = "" #your output dataset
os.makedirs(output_path, exist_ok=True)

datagen = ImageDataGenerator(
    rotation_range=10,  
    brightness_range=[0.7, 1.3],  
    shear_range=0.1,  
    zoom_range=0.4, 
    horizontal_flip=True,  
    fill_mode='nearest' 
)
  
for person_id in os.listdir(input_path):
    person_folder = os.path.join(input_path, person_id)
    if os.path.isdir(person_folder):
        person_output_folder = os.path.join(output_path, person_id)
        os.makedirs(person_output_folder, exist_ok=True)

        for filename in os.listdir(person_folder):
            file_path = os.path.join(person_folder, filename)
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                img = image.load_img(file_path)
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)

                i = 0
                for batch in datagen.flow(x, batch_size=1, save_to_dir=person_output_folder, save_prefix='aug',
                                          save_format='jpeg'):
                    i += 1
                    if i > 5: 
                        break
