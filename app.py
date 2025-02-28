from flask import Flask, render_template, request, jsonify
import torch
import joblib
import tensorflow as tf
import torch

def load_model(checkpoint_path, num_classes):
    model = torch.load(checkpoint_path, map_location=torch.device('cpu'))
    model.eval()
    return model

# Use the function to load your model
disease_model = load_model("trained_model.pth", 10)


# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')

# Load models
print("🔄 Loading models...")
disease_model = torch.load("trained_model.pth", map_location=torch.device('cpu'))
disease_model.eval()

recommendation_model = joblib.load("DecisionTree.pkl")

voting_classifier = tf.keras.models.load_model("voting_classifier.h5")

print("✅ Models loaded successfully!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    try:
        data = request.json
        input_tensor = torch.tensor(data["input"]).unsqueeze(0)
        with torch.no_grad():
            output = disease_model(input_tensor)
        prediction = output.argmax(dim=1).item()
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/recommend_plant', methods=['POST'])
def recommend_plant():
    try:
        data = request.json
        prediction = recommendation_model.predict([data["features"]])[0]
        return jsonify({"recommended_plant": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/classify_voting', methods=['POST'])
def classify_voting():
    try:
        data = request.json
        prediction = voting_classifier.predict([data["features"]])[0]
        return jsonify({"classification": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
