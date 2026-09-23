from flask import Flask, send_file, render_template

# app=Flask(__name__,template_folder="customer_template")
app = Flask(__name__)


@app.route("/")
def home():
    # link ai model <>
    return render_template("home.html")


if __name__ == "__main__":
    # app.run(debug=True,port=4040)
    app.run(debug=True)