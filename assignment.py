from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running and available!"

if __name__ == "__main__":
    # Start the Flask development server
    app.run(host="0.0.0.0", port=5000)
