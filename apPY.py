from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello World"

@app.route("/ai", methods=["POST"])
def run_ai():
    data = request.json
    G1 = data.get("G1")
    G2 = data.get("G2")
    G3 = data.get("G3")

    try:
        process = subprocess.Popen(['python', './LVali.py', str(G1), str(G2), str(G3)], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        return jsonify(status=True, msg=output.decode())
    except Exception as e:
        return jsonify(status=False, msg=str(e)), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)

