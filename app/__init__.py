import os
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from tempfile import mkdtemp
from functools import wraps
from cs50 import SQL

from tempfile import mkdtemp

from cs50 import SQL

from werkzeug.security import generate_password_hash, check_password_hash


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Ensure templates are auto-reloaded
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # load database
    db_path = os.path.join(app.instance_path, "colors.db")

    # Configure CS50 Library to use SQLite database
    db = SQL(f"sqlite:///{db_path}")

    # Ensure responses aren't cached
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    # Configure session to use filesystem (instead of signed cookies)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_FILE_DIR"] = os.path.join(app.instance_path, "flask_session")
    app.config["SESSION_FILE_THRESHOLD"] = 5
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    def login_required(f):
        """
        Decorate routes to require login.

        https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
        """

        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get("user_id") is None:
                return redirect("/login")
            return f(*args, **kwargs)

        return decorated_function

    def apology(message, code=400):
        """Render message as an apology to user."""

        def escape(s):
            """
            Escape special characters.

            https://github.com/jacebrowning/memegen#special-characters
            """
            for old, new in [
                ("-", "--"),
                (" ", "-"),
                ("_", "__"),
                ("?", "~q"),
                ("%", "~p"),
                ("#", "~h"),
                ("/", "~s"),
                ('"', "''"),
            ]:
                s = s.replace(old, new)
            return s

        return render_template("apology.html", top=code, bottom=escape(message)), code

    @app.route("/", methods=["GET", "POST"])
    @login_required
    def index():
        if request.method == "POST":
            pallet_id = request.form.get("pallet_id")

            db.execute("DELETE FROM colors WHERE id = ?", pallet_id)
            return redirect("/")

        colors = db.execute("SELECT * FROM colors WHERE user_id=?", session["user_id"])

        return render_template("index.html", colors=colors)

    @app.route("/make", methods=["GET", "POST"])
    @login_required
    def make():
        if request.method == "POST":
            pallet_name = request.form.get("pallet_name")
            if not pallet_name:
                return apology("You need to provide a pallet name to save the pallet")
            clr1 = request.form.get("clr1")
            clr2 = request.form.get("clr2")
            clr3 = request.form.get("clr3")
            clr4 = request.form.get("clr4")
            clr5 = request.form.get("clr5")

            db.execute(
                "INSERT INTO colors (user_id, pallet_name, clr1, clr2,clr3,clr4,clr5) VALUES(?,?,?,?,?,?,?)",
                session["user_id"],
                pallet_name,
                clr1,
                clr2,
                clr3,
                clr4,
                clr5,
            )
            return redirect("/")
        default_pallet = {
            "clr1": "#ff0080",
            "clr2": "#ffff80",
            "clr3": "#00ff80",
            "clr4": "#00A0ff",
            "clr5": "#00A000",
        }
        return render_template("make.html", pallet=default_pallet)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        """Log user in"""
        # Forget any user_id
        session.clear()

        # User reached route via POST (as by submitting a form via POST)
        if request.method == "POST":
            # Ensure username was submitted
            if not request.form.get("username"):
                return apology("must provide username", 403)

            # Ensure password was submitted
            elif not request.form.get("password"):
                return apology("must provide password", 403)

            # Query database for username
            rows = db.execute(
                "SELECT * FROM users WHERE username = ?", request.form.get("username")
            )

            # Ensure username exists and password is correct
            if len(rows) != 1 or not check_password_hash(
                rows[0]["hash"], request.form.get("password")
            ):
                return apology("invalid username and/or password", 403)

            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]

            # Redirect user to home page
            return redirect("/")

        # User reached route via GET (as by clicking a link or via redirect)
        else:
            return render_template("login.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            confirmation = request.form.get("confirmation")
            """Register user"""
            # Ensure username was provided
            if not username:
                return apology("must provide username", 400)

            # Ensure password was provided
            elif not password:
                return apology("must provide password", 400)

            # Ensure correct password confirmation was provided
            elif not password == confirmation:
                return apology("Passwords do not match", 400)

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?", username)

            # Ensure username does not exist in database
            if len(rows) == 1:
                return apology("username already exist", 400)
            else:
                db.execute(
                    "INSERT INTO users (username, hash) VALUES(?, ?)",
                    username,
                    generate_password_hash(password),
                )
                return redirect("/login")

        return render_template("register.html")

    @app.route("/logout")
    def logout():
        """Log user out"""

        # Forget any user_id
        session.clear()

        # Redirect user to login form
        return redirect("/")

    @app.route("/password", methods=["GET", "POST"])
    @login_required
    def password():
        """change password."""
        if request.method == "POST":
            current_pass = request.form.get("password-current")
            new_pass = request.form.get("password-new")
            confirmation = request.form.get("confirmation")
            userid = session["user_id"]

            # Ensure current password was provided
            if not current_pass:
                return apology("must provide current password", 403)

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE id = ?", userid)

            # check if current password is currect
            if not check_password_hash(rows[0]["hash"], current_pass):
                return apology("invalid current password", 403)

            # Ensure new password was provided
            if not new_pass:
                return apology("new password missing", 403)

            # Ensure correct password confirmation was provided
            if not new_pass == confirmation:
                return apology("new passwords do not match", 403)

            # update password
            db.execute(
                "UPDATE users SET hash=? WHERE id=?",
                generate_password_hash(new_pass),
                userid,
            )

            # clear session
            session.clear()
            return redirect("/login")

        return render_template("password.html")

    return app
