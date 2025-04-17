import cv2
import numpy as np
import os
from keras_facenet import FaceNet
from mtcnn import MTCNN
from scipy.spatial.distance import cosine

# Klasörler
embedding_path = "embeddings"

# ID → name match
user_labels = {
    "1": "",
    "2": "",
    # ...
}

embedder = FaceNet()
detector = MTCNN()

known_embeddings = {}
for file in os.listdir(embedding_path):
    if file.endswith(".npy"):
        user_id = file.split(".")[0]
        embeddings = np.load(os.path.join(embedding_path, file), allow_pickle=True)
        known_embeddings[user_id] = embeddings

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detector.detect_faces(frame)

    for face in faces:
        x, y, w, h = face['box']
        x, y = max(0, x), max(0, y)
        face_img = frame[y:y+h, x:x+w]
        try:
            face_img = cv2.resize(face_img, (160, 160))
        except:
            continue

        face_embedding = embedder.embeddings([face_img])[0]

        identity = "Taninmiyor"
        min_dist = 0.6  # eşik değer

        for user_id, embeddings in known_embeddings.items():
            for ref_emb in embeddings:
                dist = cosine(face_embedding, ref_emb)
                if dist < min_dist:
                    min_dist = dist
                    identity = user_labels.get(user_id, f"Kullanici {user_id}")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, identity, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
