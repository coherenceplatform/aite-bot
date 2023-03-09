from ai_logic import (
    generate_plan,
    word_count,
)
from flask import Flask, request, render_template, session, redirect
import os
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    uploaded_file = request.files["file"]

    _uploaded = uploaded_file.read()
    if word_count(_uploaded) > 3000:
        raise BadRequest

    plan = generate_plan(_uploaded)
    return render_template("index.html", test_plan=plan)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)
