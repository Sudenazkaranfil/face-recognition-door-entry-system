import json
from bcrypt import hashpw, gensalt
from connection import get_connection

def hash_password(password):
    return hashpw(password.encode(), gensalt()).decode()

def hash_tr_id(tr_id_no):
    return hashpw(tr_id_no.encode(), gensalt()).decode()

def insert_users_from_json():
    with open("users.json", "r", encoding="utf-8") as f:
        users_data = json.load(f)

    conn = get_connection()
    cursor = conn.cursor()

    for user in users_data:
        hashed_tr_id_no = hash_tr_id(user["tr_id_no"])
        hashed_password = hash_password(user["password"])

        cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (user["email"],))
        count = cursor.fetchone()[0]

        if count == 0:  
            sql = """
            INSERT INTO users (tr_id_no, first_name, last_name, email, password_hash, role)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (hashed_tr_id_no, user["first_name"], user["last_name"], user["email"], hashed_password, user["role"])

            cursor.execute(sql, values)
            print(f"Kullanıcı {user['first_name']} {user['last_name']} başarıyla eklendi.")
        else:
            print(f"E-posta {user['email']} zaten mevcut, kullanıcı eklenmedi.")

    conn.commit()

    cursor.close()
    conn.close()
