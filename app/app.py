from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Hello from DevOps pet project!",
        "environment": os.getenv("APP_ENV", "development")
    }

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)