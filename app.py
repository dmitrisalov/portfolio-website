from flask import Flask, render_template

# Create the application
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html", title="Home")

# Page for Pong.
@app.route("/pong")
def pong():
    return render_template("pong.html", title="Pong")

# Page for Infinity Cube.
@app.route("/infinity-cube")
def infinity_cube():
    return render_template("infinity_cube.html", title="Infinity Cube")

# Page for Terrain Generator.
@app.route("/terrain-generator")
def terrain_generator():
    return render_template("terrain_generator.html", title="Terrain Generator")

# For dev environment purposes
if __name__ == "__main__":
    app.run()