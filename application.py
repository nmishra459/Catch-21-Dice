import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///dice.db")
#db = SQL(os.getenv("DATABASE_URL"))


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must enter username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must enter password")

        # Query database for username

        # Ensure username exists and password is correct
        elif len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Username and/or Password is incorrect")
        else:
            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]
            # Redirect user to home page
            return redirect("/")

        return render_template("login.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user for an account."""

    # POST
    if request.method == "POST":

        # Validate form submission
        if not request.form.get("username"):
            flash("Please provide username")
            return render_template("register.html")
        elif not request.form.get("password"):
            flash("Please provide password")
            return render_template("register.html")
        elif request.form.get("password") != request.form.get("confirmation"):
            flash("password and confirmation don't match")
            return render_template("register.html")

        # Add user to database
        try:
            id_table = db.execute("SELECT id FROM users")
            #max_value = max(id_table.values())
            table = []
            for i in range(len(id_table)):
                table.append(id_table[i]["id"])
            if not id_table:
                max_id = 0
            else:
                max_id = max(table)+1

            id = db.execute("INSERT INTO users (id, username, hash) VALUES(?, ?, ?)",
                            max_id,
                            request.form.get("username"),
                            generate_password_hash(request.form.get("password")))
        except RuntimeError:
            flash("username taken")
            return render_template("register.html")

        # Log user in
        session["user_id"] = max_id

        # Let user know they're registered
        flash("Registered!")
        return redirect("/")

    # GET
    else:
        return render_template("register.html")

@app.route("/change", methods=["GET", "POST"])
@login_required
# Allows user to change password
def change():
    if request.method == "POST":

        # Ensure password was submitted
        password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        new_confirmation = request.form.get("new_confirmation")

        if not password:
            flash("Must enter password")
        # Ensures the password was the right password
        elif not check_password_hash(db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]["hash"], password):
            flash("Incorrect 'current password' entered")
        # Ensures new password/confirmation was submitted
        elif not new_password:
            flash("Must provide new password")
        elif not new_confirmation:
            flash("Must provide confirmation")
        # Checks if password matches confirmation
        elif new_password != new_confirmation:
            flash("New password and confirmation don't match")
        else:
            new_password = generate_password_hash(new_password)
            # updates user profile with hashed password
            db.execute("UPDATE users SET hash = ?  WHERE id = ?", new_password, session["user_id"])
            # Redirect user to home page
            flash("Success! Password changed.")
            return redirect("/")

        return render_template("change.html")

    else:
        return render_template("change.html")


@app.route("/second_login", methods=["GET", "POST"])
def second_login():
    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensures username was submitted
        player_two = request.form.get("username")
        if not player_two:
            flash("Must enter username")
        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must enter password")
        # Ensure username exists and password is correct
        elif len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Username and/or Password is incorrect")
        # Makes sure that the second account credentials don't match the first account credentials
        elif session["user_id"] == rows[0]["id"]:
            flash("That account is already logged in. Please log in a different account.")
        # Redirect user to the play page
        else:
            player_one = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]
            return render_template("play.html", player_one_name=player_one, player_two_name=player_two)

        return render_template("second_player_login.html")

    else:
        return render_template("second_player_login.html")


@app.route("/guest", methods=["GET", "POST"])
# code sequence for when player two decides to play as a guest (unregistered user)
def guest():
    if request.method == "POST":
        player_one = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]
        player_two = "Guest"
        return render_template("play.html", player_one_name=player_one, player_two_name=player_two)
    else:
        return render_template("second_player_login.html")


@app.route("/end_match", methods=["GET", "POST"])
def end():
    if request.method == "POST":
        p1_wins = request.form.get("player1-wins")
        if not p1_wins:
            p1_wins = 0

        p1_losses = request.form.get("player1-losses")
        if not p1_losses:
            p1_losses = 0

        total_games = int(p1_wins) + int(p1_losses)

        # Updates all the aggregated stats for the user
        db.execute("UPDATE users SET total_wins = total_wins + ? WHERE id = ?", int(p1_wins), session['user_id'])
        db.execute("UPDATE users SET total_losses = total_losses + ? WHERE id = ?", int(p1_losses), session['user_id'])
        db.execute("UPDATE users SET total_played = total_played + ? WHERE id = ?", int(p1_losses) + int(p1_wins), session['user_id'])

        p1_name = request.form.get("p1-name")
        p2_name = request.form.get("p2-name")

        # Updates the currently logged in player's play history
        db.execute("INSERT INTO play_history (id, time, opponent, games_played, games_won, games_lost) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], datetime.now().strftime('%Y-%m-%d %H:%M:%S'), p2_name, total_games, p1_wins, p1_losses)

        # Only updates the other player's play history if they are NOT a guest
        if p2_name != 'Guest':
            p2_id = db.execute("SELECT id FROM users WHERE username = ?", p2_name)[0]["id"]
            p2_wins = request.form.get("player2-wins")
            if not p2_wins:
                p2_wins = 0

            p2_losses = request.form.get("player2-losses")
            if not p2_losses:
                p2_losses = 0

            db.execute("UPDATE users SET total_wins = total_wins + ? WHERE id = ?", int(p2_wins), p2_id)
            db.execute("UPDATE users SET total_losses = total_losses + ? WHERE id = ?", int(p2_losses), p2_id)
            db.execute("UPDATE users SET total_played = total_played + ? WHERE id = ?", int(p2_wins) + int(p2_losses), p2_id)
            db.execute("INSERT INTO play_history (id, time, opponent, games_played, games_won, games_lost) VALUES (?, ?, ?, ?, ?, ?)",
                       p2_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), p1_name, total_games, p2_wins, p2_losses)

        flash("The match is complete! Check the leaderboard for updated results.")
        return redirect("/")
    else:
        return redirect("/")


@app.route("/stats", methods=["GET", "POST"])
@login_required
def stats():
    stats = db.execute("SELECT * FROM play_history WHERE id = ? ORDER BY time DESC", session["user_id"])

    if not stats:
        flash("You don't have any stats yet. Play some games first!")
        return render_template("index.html")

    return render_template("stats.html", stats=stats)


@app.route("/leaderboard")
@login_required
def leaderboard():

    # stores rows of the leaderboard table in the leaderboard variable, ranked by number of wins
    leaderboard = db.execute("SELECT * FROM users ORDER BY total_wins DESC")
    return render_template("leaderboard.html", leaderboard=leaderboard)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
