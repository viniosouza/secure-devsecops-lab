from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "App Vulnerável Rodando"

# ❌ SQL Injection
@app.route("/login")
def login():
    user = request.args.get("user")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{user}'"
    cursor.execute(query)

    return "Login executado"

# ❌ XSS
@app.route("/hello")
def hello():
    name = request.args.get("name")
    return f"<h1>Olá {name}</h1>"

# ❌ Broken Access Control
@app.route("/admin")
def admin():
    return "Área admin sem autenticação"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)