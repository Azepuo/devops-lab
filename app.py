from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Version Finale - Pipeline DevOps OK (Docker + K8S) - Tout est automatique !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
