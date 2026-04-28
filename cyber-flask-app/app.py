from flask import Flask, render_template, request
import sqlite3
import datetime

app = Flask(__name__)


def log_attempt(username):
    with open("logs/access.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - Login attempt: {username}\n")


@app.route('/')
def login():
    return render_template('login.html')

#  VULNERABLE LOGIN (SQL Injection)


@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    log_attempt(username)

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Vulnerable query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = c.execute(query).fetchone()

    if result:
        return render_template('dashboard.html', user=username)
    else:
        return "Login Failed"

# SECURE LOGIN (Safe version)


@app.route('/secure-login', methods=['POST'])
def secure_login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Parameterized query (safe)
    query = "SELECT * FROM users WHERE username=? AND password=?"
    result = c.execute(query, (username, password)).fetchone()

    if result:
        return f"Secure Login Success: {username}"
    else:
        return "Secure Login Failed"


if __name__ == '__main__':
    app.run(debug=True)
