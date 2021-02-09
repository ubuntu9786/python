from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# just a / stands for the main directory of the website
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def about(name):
    return render_template("name.html", content=name)

@app.route("/looser")
def looser():
    return "<h1> you cant visit that page pfft</h1>"


@app.route("/admin")
def admin():
    return redirect(url_for("looser"))

if __name__ == "__main__":
    app.run(debug=True)
