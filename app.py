
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Create home page
@app.route("/")
def hello():
    return "Hello, World! Welcome to Flask Application."

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
