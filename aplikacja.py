from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import sqlite3

app = Flask(__name__)

# generowanie klucza do szyfrowania
key = Fernet.generate_key()
cipher = Fernet(key)

# ustawienia bazy danych
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET"])
def home():
    return "Witam na stronie"

# szyfrowanie wiadomości
@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    message = data.get("message", "")
    encrypted_message = cipher.encrypt(message.encode()).decode()
    return jsonify({"encrypted_message": encrypted_message})

#deszyfrowanie wiadomości
@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    encrypted_message = data.get("encrypted_message", "")
    decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()
    return jsonify({"decrypted_message": decrypted_message})

# logowanie z możliwością wstrzykiwania SQL
@app.route("/vulnerable-login", methods=["POST"])
def vulnerable_login():
    data = request.json
    username = data.get("username", "")
    password = data.get("password", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    if user:
        return jsonify({"message": "Login successful (vulnerable endpoint)"})
    return jsonify({"message": "Invalid credentials"})

# bezpieczne logowanie bez możliwosci wstrzykiwania SQL
@app.route("/secure-login", methods=["POST"])
def secure_login():
    data = request.json
    username = data.get("username", "")
    password = data.get("password", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return jsonify({"message": "Login successful (secure endpoint)"})
    return jsonify({"message": "Invalid credentials"})

if __name__ == "__main__":
    app.run(debug=True)
