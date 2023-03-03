from flask import Flask, request, render_template, session, redirect
import os

from main import (
    generate_plan,
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/generate', methods=["POST"])
def generate():
    uploaded_file = request.files["file"]
    plan = generate_plan(uploaded_file.read())
    return render_template("index.html", test_plan=plan)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True)

