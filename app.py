from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from cs50 import SQL
from helpers import login_required, generate_password
from werkzeug.security import check_password_hash, generate_password_hash

# Config the flask app
app = Flask(__name__)

# Config the session
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
Session(app)

# Data base
db = SQL("sqlite:///data.db")

# index.html
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.form.get("delete_btn"):
        db.execute("DELETE FROM passwords WHERE site = ?", request.form.get("delete_btn"))
    passwords = db.execute("SELECT * FROM passwords WHERE person_id = ?", session["user_id"])
    return render_template("index.html", passwords=passwords)


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        user_name = request.form.get("username")
        password = request.form.get("password")
        check = db.execute("SELECT * FROM log_in WHERE user_name = ?", user_name)
        if not user_name or len(check) != 1:
            return render_template("error.html", placeholder="Invalid Username")
        if not password or check[0]["password"] != password:
            return render_template("error.html", placeholder="Invalid Password")
        session["user_id"] = check[0]["id"]
        return redirect("/")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        re_password = request.form.get("re-password")
        if not username:
            return render_template("error.html", placeholder="Invalid Username")
        if not password:
            return render_template("error.html", placeholder="Invalid Password")
        if not re_password:
            return render_template("error.html", placeholder="Password Required")
        if not password == re_password:
            return render_template("error.html", placeholder="Passwords don't match")
        try:
            db.execute("INSERT INTO log_in(user_name, password) VALUES (?, ?)", username, password)
        except ValueError:
            return render_template("error.html", placeholder="This Username is used")
        return redirect("/login")
    return render_template("register.html")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        site_name = request.form.get("sitename")
        site_username = request.form.get("username")
        site_password = generate_password(length=15)
        db.execute("INSERT INTO passwords(person_id, user_name, password, site) VALUES (?, ?, ?, ?)", session["user_id"], site_username, site_password, site_name.capitalize())
        return redirect("/")
    return render_template("add.html")


@app.route("/table", methods=["GET", "POST"])
@login_required
def table():
    rows = db.execute("SELECT * FROM passwords WHERE person_id = ?", session["user_id"])
    return render_template("table.html", rows=rows)


@app.route("/search", methods=["POST", "GET"])
@login_required
def search():
    q = request.args.get("q")
    passwords = db.execute("SELECT * FROM passwords WHERE person_id = ? AND site LIKE ?", session["user_id"], f"%{q}%".capitalize())
    if request.form.get("delete_btn"):
        db.execute("DELETE FROM passwords WHERE site = ?", request.form.get("delete_btn"))
    return render_template("search.html", passwords=passwords)