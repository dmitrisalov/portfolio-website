from flask import Flask, render_template

# Create the application
app = Flask(__name__)

# Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

# For dev environment purposes
if __name__ == "__main__":
    app.run()