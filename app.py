from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier origen (como tu frontend)

@app.route("/api/mensaje", methods=["GET"])
def mensaje():
    return jsonify({"mensaje": "Hola desde el backend Flask!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
