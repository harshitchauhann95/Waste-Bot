from flask import Flask, request, jsonify
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import io
import random
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ Fixes 403 Forbidden issues

# Load AI models
from torchvision.models import resnet18, ResNet18_Weights

image_classifier = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
image_classifier.eval()

text_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
candidate_labels = ["recyclable", "non-recyclable", "compostable"]

# Image transformation function
def transform_image(image_bytes):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    return transform(image).unsqueeze(0)

@app.route("/classify_image", methods=["POST"])
def classify_image():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400  # ✅ JSON response

    try:
        img_bytes = file.read()
        img_tensor = transform_image(img_bytes)

        with torch.no_grad():
            output = image_classifier(img_tensor)
        
        probabilities = F.softmax(output[0], dim=0)
        predicted_class = torch.argmax(probabilities).item()

        # Mapping to waste categories (dummy mapping)
        categories_map = {0: "recyclable", 1: "non-recyclable", 2: "compostable"}
        category = categories_map.get(predicted_class % 3, "unknown")

        return jsonify({"category": category, "instructions": f"Dispose in {category} bin."})

    except Exception as e:
        return jsonify({"error": f"Failed to classify image: {str(e)}"}), 500

@app.route("/classify_text", methods=["POST"])
def classify_text():
    data = request.get_json()
    text = data.get("description", "")
    if not text:
        return jsonify({"error": "No description provided"}), 400

    try:
        result = text_classifier(text, candidate_labels)
        category = result['labels'][0]
        return jsonify({"category": category, "instructions": "Follow proper disposal guidelines."})
    except Exception as e:
        return jsonify({"error": f"Failed to classify text: {str(e)}"}), 500

@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    leaderboard_data = [
        {"name": "Alice", "points": 120},
        {"name": "Bob", "points": 95},
        {"name": "Charlie", "points": 85}
    ]
    return jsonify(leaderboard_data)

@app.route("/reward", methods=["POST"])
def reward_user():
    data = request.get_json()
    user = data.get("user", "Unknown")
    points = random.randint(5, 20)
    return jsonify({"user": user, "points_awarded": points, "message": "Points added successfully!"})

if __name__ == "__main__":
    app.run(debug=True)