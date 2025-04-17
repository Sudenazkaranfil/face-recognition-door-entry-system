# predict_face_from_image.py

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Eğitilen modelin yolunu ver
model_path = 'face_recognition_model.h5'  # Model dosyasını daha önce bu adla kaydetmiştik
model = load_model(model_path)

# Eğitim sırasında kullanılan sınıf isimleri (mapping)
class_names = ['Fatih', 'Derya', 'Aysun', 'Neslihan', 'Şükran', 'Senem', 'Yeliz Sude']  # Bunları senin sınıflarına göre güncelle

# Test etmek istediğimiz görsellerin yolları
image_paths = ['face_dataset/1/fatih_kar_facedata2.jpg', 'face_dataset/2/derya_berikten_facedata2.jpg', 'face_dataset/6/senem_suel_facedata2.jpg']

for image_path in image_paths:
    # Görseli modelin beklediği boyuta getir (150x150)
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # (1, 150, 150, 3)
    img_array = img_array / 255.0  # Normalize

    # Tahmin yap
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_name = class_names[predicted_class_index]

    # Tahmin sonucunu yazdır
    print(f"Test edilen görsel: {image_path}")
    print(f"Tahmin edilen kişi: {predicted_class_name}")
    print(f"Probabilities: {predictions[0]}")
    print("\n")

