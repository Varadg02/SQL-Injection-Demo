# 🛡️ SQL Injection Demonstration (Educational Purpose Only)

This project demonstrates how SQL Injection (SQLi) vulnerabilities occur in poorly coded web applications and how to fix them using secure coding practices. It uses a simple Flask app with a login form connected to an SQLite database.

---

## 🎯 Objective

- Simulate a vulnerable login form that allows SQL Injection.
- Demonstrate how malicious users can bypass authentication.
- Show how to fix the issue using parameterized queries.
- Spread awareness of secure coding practices.

---

## 🧰 Requirements

- Python 3.x
- Flask
- SQLite3 (included in Python)
- Web browser

---

## 📁 Project Structure

sql_injection_demo/
├── app.py # Main Flask application (vulnerable version)
├── init_db.py # Script to initialize SQLite database
├── templates/
│ ├── login.html # HTML login form
│ └── dashboard.html # Page shown after successful login
├── users.db # SQLite database (generated)
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. 📦 Install Flask

```bash
pip install flask
2. 🏗️ Initialize the Database
Run this script to create users.db and a default user:

bash
Copy
Edit
python init_db.py
It will add a user:

Username: admin

Password: admin123

3. 🚀 Run the App
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000

🧪 Vulnerability Demonstration
✅ Normal Login
Use:

Username: admin

Password: admin123

✔️ This logs in successfully.

❌ Failed Login
Try:

Username: admin

Password: wrongpass

❌ Login fails.

🔓 SQL Injection Bypass
Try:

Username: admin' --

Password: (anything or leave blank)

Query becomes:

sql
Copy
Edit
SELECT * FROM users WHERE username = 'admin' --' AND password = ''
✔️ The -- comments out the password check, allowing access!

🔐 How to Fix the Vulnerability
Replace this code in app.py:

python
Copy
Edit
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
c.execute(query)
With this secure version:

python
Copy
Edit
c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
✅ This uses parameterized queries, which prevent SQL code from being injected.

📚 Awareness Material
🔒 Safe Coding Practices
Always use parameterized queries or ORM (e.g., SQLAlchemy, Django ORM).

Validate user input strictly.

Never concatenate untrusted data into SQL queries.

Enforce least privilege on database accounts.

Enable logging and monitor suspicious access.
