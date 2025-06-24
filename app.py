from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect (
    host="localhost",
    user="root",
    password="manoj1196",
    database="flaskapp"
)
cursor = db.cursor()

@app.route("/")
def home():
    return redirect("/login")

@app.route("/dashboard/<username>")
def dashboard(username):
    return render_template("dashboard.html", username=username)


@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            return render_template("message.html", message="Username already exists", redirect_url=url_for('signup'))
        elif password != confirm:
            return "Password does not match, try again"
        elif username.lower() in password.lower():
            return "Password should not be same as username. Choose strong password"
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            return redirect(url_for('dashboard', username=username))
    return render_template("signup.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            return redirect(url_for('dashboard', username=username))
        else:
            return render_template("message.html", message="Invalid username or password", redirect_url=url_for('login'))

    return render_template("login.html")

if __name__ == "__main__":
    
    app.run(debug=True)        
    