from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Lokesh! This is my DevOps Git practice app."

@app.route("/about")
def about():
    return "Learning Git for DevOps."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
