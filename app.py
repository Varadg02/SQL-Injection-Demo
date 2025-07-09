# app.py
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # ❌ VULNERABLE: Direct string formatting
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Running Query:", query)
    c.execute(query)

    user = c.fetchone()
    conn.close()

    if user:
        return render_template('dashboard.html', username=username)
    else:
        return "Login Failed. Try again."

if __name__ == '__main__':
    app.run(debug=True)
