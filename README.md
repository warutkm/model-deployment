# model-deployment
# AgriAI Project

AgriAI is a Flask-based web application designed to assist farmers by integrating multiple machine learning models for plant disease detection, plant recommendation, and weather prediction.

## 🚀 Features
- **Plant Disease Detection**: Uses a deep learning model to identify plant diseases from images.
- **Plant Recommendation**: Suggests suitable crops based on environmental factors.
- **Weather Prediction**: Provides weather-based recommendations.
- **User-Friendly Web Interface**: Built with HTML, CSS, and Flask for a seamless experience.

## 📂 Project Structure
```
AgriAI_Project/
│── static/                     # CSS, images, videos
│── templates/                   # HTML templates
│── models/                      # Machine learning models
│   │── trained_model.pth        # PyTorch model for disease detection
│   │── DecisionTree.pkl         # Plant recommendation model
│   │── voting_classifier.h5     # Weather classification model
│── app.py                       # Flask backend
│── requirements.txt             # Dependencies
│── Procfile                     # Deployment configuration
│── README.md                    # Project documentation
```

## 🛠 Setup Instructions
### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Run the Flask App
```sh
python app.py
```
Then, open `http://127.0.0.1:5000/` in your browser.

### 3️⃣ Deploy on Render
1. Push your project to GitHub.
2. Sign up on [Render](https://render.com/).
3. Create a **new Web Service**, connect GitHub, and deploy with `gunicorn app:app`.

## 🧩 API Endpoints
- `/predict_disease` → **POST** (Predicts plant disease)
- `/recommend_plant` → **POST** (Recommends suitable crops)
- `/classify_voting` → **POST** (Performs weather classification)

## 💡 Future Enhancements
- Add real-time image processing for plant disease detection.
- Integrate live weather API.
- Improve UI design.

## 📜 License
This project is open-source and available under the MIT License.

---
💻 Developed by KEYBIARD CRACKERS 🚀

