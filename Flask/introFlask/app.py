from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello this is my flask server"


@app.route("/about")
def about():
    return "This is the about us section"


@app.route("/pic")
def get_pic():
    file_path = "one.png"
    return send_file(file_path)


if __name__ == "__main__":
    app.run(debug=True)