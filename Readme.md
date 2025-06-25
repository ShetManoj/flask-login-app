# 🔐 Flask Login App

A beginner-friendly yet functional **user authentication system** built using **Python**, **Flask**, and **MySQL**.  
This web app allows users to **sign up**, **log in**, and get redirected to a **personalized dashboard** with form validations, password checks, and error handling.

---

## 🚀 Overview

This project was created to understand the fundamentals of **Flask web development**, including:
- Routing and form handling
- HTML template rendering
- Data persistence using text files and later, a relational database
- User authentication flow

Originally designed with a simple text file for data storage, the application was later **upgraded to use a MySQL database** to mimic real-world practices.

---

## ✨ Features

✅ User Sign-Up  
✅ Password confirmation and validation  
✅ Username uniqueness check  
✅ Password should not contain the username  
✅ User Login  
✅ Dashboard upon successful login  
✅ Error messages shown on invalid actions  
✅ Redirects back to signup/login after errors  
✅ Simple UI with light/dark theme toggle  
✅ HTML templates with embedded Flask logic  
✅ Switched from `.txt` storage to MySQL  

---

## 🛠 Tech Stack

| Layer        | Tools Used                      |
|--------------|---------------------------------|
| **Frontend** | HTML, CSS, JS (for theme toggle)|
| **Backend**  | Python, Flask                   |
| **Database** | MySQL (via `mysql-connector-python`)|

---

## 🔄 Migration: Text File → MySQL Database

This app initially stored users in a `users.txt` file like: username,password for example abc,456


However, to introduce more secure, scalable, and realistic user data handling, the system was upgraded to use **MySQL**.

### 🧾 Reason for the Upgrade

- `.txt` files are not reliable or secure  
- No support for indexing, queries, or relationships  
- Risk of file corruption or data loss  
- MySQL allows persistent, structured storage  
- Aligns with industry-standard backend development  

---

## 🧰 Database Setup

The database used is called `flaskapp`, with a single table named `users`.

### SQL Schema:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);


