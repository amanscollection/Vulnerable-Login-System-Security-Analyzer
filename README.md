Cybersecurity Flask App 

Overview  
This project is a vulnerable web application built using Flask to demonstrate common security flaws such as SQL Injection and how to fix them using secure coding practices.  

Features  
* Vulnerable Login System (SQL Injection)
* Secure Login System (Parameterized Queries)
* Logging of Login Attempts
* Simple Dashboard

Tech Stack  
* Python
* Flask
* SQLite

Installation  
* git clone https://github.com/amanscollection/cyber-flask-app.git
* cd cyber-flask-app
* pip install -r requirements.txt
* python app.py

Usage  
* Open browser: http://127.0.0.1:5000  

SQL Injection Demo  
* Try this payload:
  admin
  
This bypasses authentication in the vulnerable login.


# Vulnerable-Login-System-Security-Analyzer
Built using Flask while Vulnerable Login System + Security Analyzer problem-solutions.

# Project Detials
This project demonstrates:

* SQL Injection vulnerability
* Secure vs insecure coding
* Logging & basic attack detection

# Project Structure
STEP 1: Project Structure

cyber-flask-app/  
│── app.py  
│── database.db  
│── templates/  
│   ├── login.html  
│   ├── dashboard.html  
│── logs/  
│   └── access.log  
│── static/  
│── requirements.txt  
│── README.md  

# Install Requirements

STEP 2: Install Requirements  
  pip install flask
  
  Create requirements.txt:
  Flask

# Create Database  
STEP 3: Create Database  

Run Python shell

# Flask App
STEP 4: Main Flask App (app.py)

# HTML and dashboard Templates  
STEP 5: HTML Templates  

  login.html  
  dashboard.html  

# Run Python Project  
STEP 6: Run Project  

  python app.py  
  Open: http://127.0.0.1:5000  

# SQL Injection
STEP 7: Test SQL Injection  

  Try login with:  
    username: admin'  
    password: anything

Error:  
<img width="1403" height="856" alt="image" src="https://github.com/user-attachments/assets/8828a1ca-4ea6-417c-8066-ab1756f8a91c" />

