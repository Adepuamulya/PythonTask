from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Second Page
@app.route("/second")
def second():
    return render_template("second.html")

if __name__ == "__main__":
    app.run(debug=True)