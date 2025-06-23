from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

def load_users():
    try:
        with open("users.txt", "r") as f:
            for line in f:
                username,password = line.strip().split(",", 1)
                users[username] = password
    except FileNotFoundError:
        pass

def save_user(username, password):
    with open ("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

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

        if username in users:
            return render_template("message.html", message="Username already exists", redirect_url=url_for('signup'))
        elif password != confirm:
            return "Password does not match, try again"
        elif username.lower() in password.lower():
            return "Password should not be same as username. Choose strong password"
        else:
            users[username] = password
            save_user(username, password)
            return redirect(url_for('dashboard', username=username))
    return render_template("signup.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return redirect(url_for('dashboard', username=username))
        else:
            return render_template("message.html", message="Invalid username or password", redirect_url=url_for('login'))

    return render_template("login.html")

if __name__ == "__main__":
    load_users()
    app.run(debug=True)        
    