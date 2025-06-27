from flask import Flask, render_template

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Your information was submitted successfully, {name}!"
    return render_template("form.html")


import sqlite3

def save_name_to_db(name):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS guests (name TEXT)")
    c.execute("INSERT INTO guests (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('form.html', 'confirmation.html', messages=messages)
