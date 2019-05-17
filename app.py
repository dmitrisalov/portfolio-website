from flask import Flask, render_template

# Create the application
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("hello_world.html", title="Hello, world!")

# For dev environment purposes
if __name__ == "__main__":
    app.run()