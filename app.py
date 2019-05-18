from flask import Flask, render_template

# Create the application
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/pong")
def pong():
    return render_template("home.html", title="Pong")

@app.route("/infinity-cube")
def infinity_cube():
    return render_template("home.html", title="Infinity Cube")

# For dev environment purposes
if __name__ == "__main__":
    app.run()