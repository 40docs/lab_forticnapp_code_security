from flask import Flask
from config import AWS_SECRET_KEY
from vuln_app import get_user, list_files, load_data

app = Flask(__name__)

@app.route('/')
def home():
    return f"Secret: {AWS_SECRET_KEY}"

@app.route("/users")
def users():
    username = request.args.get("name")
    return {"result": get_user(username)}  # ❌ vulnerable SQL usage

@app.route("/files")
def files():
    target = request.args.get("target")
    list_files(target)  # ❌ unsanitized shell command
    return {"status": "done"}

@app.route("/load")
def load():
    data = request.args.get("payload")
    obj = load_data(data)  # ❌ unsafe deserialization
    return {"loaded": str(obj)}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
