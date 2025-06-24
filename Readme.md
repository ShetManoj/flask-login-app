# 🔐 Flask Login App

A simple web-based login and signup system built using Python and Flask.

This project handles basic user authentication with form validations, error handling, and a dashboard page after login. User data is stored in a local text file.

---

### ✨ Features

- User signup & login
- Duplicate username check
- Basic password rules
- Dashboard after login
- Error messages with redirection

## 🔄 Switched from Text File to MySQL Database

This project was originally using a `.txt` file to store user credentials temporarily. While that approach was simple for learning purposes, it lacked data persistence and security.

To improve this, the app is upgraded to use a **MySQL database** for storing users.

---

### ✅ Why the Change?
- `.txt` files are not reliable for long-term storage.
- Databases allow persistent, secure, and scalable data handling.
- Prepares the app for real-world use and future improvements.

---

### ⚙️ How It Was Done
- Installed **MySQL Community Server** and **Workbench** locally.
- Created a database named `flaskapp`.
- Inside it, created a table named `users` with the following structure:

  ```sql
  CREATE TABLE users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      username VARCHAR(255) NOT NULL UNIQUE,
      password VARCHAR(255) NOT NULL
  );

