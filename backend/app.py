from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_disease

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Backend is running"

@app.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:   # ✅ FIXED
        return jsonify({"error": "No image"}), 400

    image = request.files["image"]     # ✅ FIXED
    disease = predict_disease(image)

    return jsonify({"disease": disease})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
