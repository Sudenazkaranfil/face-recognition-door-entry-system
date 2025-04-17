# Face Recognition-Based Door Entry System 🚪🧠

## 🌍EN

### Overview
This project implements a real-time face recognition system designed for door access control. Using deep learning techniques such as FaceNet for facial embedding and MTCNN for face detection, the system is able to recognize authorized individuals and grant them access automatically. It also integrates with a simple user management system, allowing you to add new users and manage the database.

⚠️ Privacy Notice: Real user data (e.g., images, names) has been excluded for privacy and security reasons. To fully utilize the system, you will need to add your own data to sections like 'users.json', where user-specific information is stored.

### Technologies Used
Python

OpenCV

MTCNN (Face Detection)

FaceNet (Face Recognition)

Keras & TensorFlow

PostgreSQL (Database)

### Features
Real-time face recognition using a webcam or images

Add and remove users from the system

Face embeddings for efficient recognition

Easy integration with other access control systems

### File Descriptions
data_augmentation.py: Contains functions to augment the dataset (e.g., flipping, rotating) to improve the model's performance.

embedding.py: Generates facial embeddings using FaceNet to represent faces in a compact form, used for comparison during recognition.

face_recognition.py: Implements the face recognition functionality using FaceNet and MTCNN for face detection.

face_recognition_model.py: Contains the pre-trained model and logic to perform the face recognition task.

predict_face_from_image.py: Script for predicting a face from a given image.

connection.py: Database connection script to connect to PostgreSQL for user data storage.

insert_users.py: A script for inserting new user data into the database.

main.py: The main script that ties everything together and runs the system.

users.json: JSON file containing the users' information.

---

## 🌍TR

### Genel Bakış
Bu proje, yüz tanıma teknolojisi kullanarak kapı giriş kontrolü sağlayan bir sistemi hayata geçirmektedir. FaceNet yüz embedding yöntemi ve MTCNN yüz tespiti algoritmalarını kullanarak, sisteme kayıtlı kişileri tanır ve giriş izni verir. Ayrıca basit bir kullanıcı yönetim sistemi de içerir, böylece kullanıcılar eklenebilir ve veritabanı yönetilebilir.

⚠️ Gizlilik Uyarısı: Gerçek kullanıcı verileri (örneğin, resimler ve isimler) gizlilik ve güvenlik sebepleriyle dahil edilmemiştir. Sistemi tam anlamıyla kullanabilmek için 'users.json' gibi dosyalardaki kullanıcı verileri içeren kısımlara kendi verilerinizi eklemeniz gerekmektedir.

### Kullanılan Teknolojiler
Python

OpenCV

MTCNN (Yüz Tespiti)

FaceNet (Yüz Tanıma)

Keras & TensorFlow

PostgreSQL (Veritabanı)

### Özellikler
Web kameradan veya görsellerden gerçek zamanlı yüz tanıma

Sisteme yeni kullanıcılar ekleme ve var olanları silme

Yüz embedding'leri ile verimli tanıma

Diğer giriş kontrol sistemlerine kolay entegrasyon

### Dosya Açıklamaları
data_augmentation.py: Modelin performansını artırmak için veri setini artırma (örneğin, görüntüleri döndürme, ters çevirme) işlevleri içerir.

embedding.py: FaceNet kullanarak yüz embedding'leri (yüz temsilcileri) oluşturur, bu veriler tanıma sırasında karşılaştırma için kullanılır.

face_recognition.py: Yüz tanıma işlevselliğini FaceNet ve MTCNN ile birlikte uygular.

face_recognition_model.py: Önceden eğitilmiş model ve yüz tanıma işlemini gerçekleştiren mantığı içerir.

predict_face_from_image.py: Verilen bir görüntüden yüz tahmini yapma için kullanılan betik.

connection.py: PostgreSQL veritabanına bağlanmak için kullanılan bağlantı betiği.

insert_users.py: Kullanıcı verilerini veritabanına eklemek için kullanılan betik.

main.py: Veritabanı sistemini birleştiren ve çalıştıran ana betik.

users.json: Kullanıcı bilgilerini içeren JSON dosyası.
