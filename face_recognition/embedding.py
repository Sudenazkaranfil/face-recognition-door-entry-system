from keras_facenet import FaceNet
from mtcnn import MTCNN
import numpy as np
import cv2
import os

embedder = FaceNet()
detector = MTCNN()

dataset_path = '' #your dataset file name
embedding_path = 'embeddings'
if not os.path.exists(embedding_path):
    os.makedirs(embedding_path)

for person in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person)
    embeddings = []

    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)
        img = cv2.imread(img_path)
        result = detector.detect_faces(img)
        if not result:
            continue
        x, y, w, h = result[0]['box']
        face = img[y:y+h, x:x+w]
        face = cv2.resize(face, (160, 160))
        face = np.asarray(face)
        emb = embedder.embeddings([face])[0]
        embeddings.append(emb)

    np.save(os.path.join(embedding_path, f"{person}.npy"), embeddings)
