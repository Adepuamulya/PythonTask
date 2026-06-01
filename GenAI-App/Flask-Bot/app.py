from flask import Flask
from routes import main

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )