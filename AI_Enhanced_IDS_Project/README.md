# 🛡️ AI-Enhanced Intrusion Detection System

## 🔍 Objective
To develop an intrusion detection system (IDS) that uses machine learning to classify network attacks from normal traffic in real time.

## 🧠 Features
- Real-time intrusion detection
- Uses Random Forest for classification
- Flask-based API for inference
- Preprocessed dataset and model serialization

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Preprocess the Dataset
```bash
python preprocess.py
```

### 3. Train the Model
```bash
python train_model.py
```

### 4. Run the Inference API
```bash
python app.py
```

### 5. Test the API
Use Postman or curl:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [0.1, 0.2, ..., 0.4]}'
```

## 📂 Project Structure
```
AI_Enhanced_IDS_Project/
├── preprocess.py
├── train_model.py
├── app.py
├── requirements.txt
├── model.joblib
├── scaler.joblib
└── README.md
```

## 📈 Sample Output
JSON:
```json
{"prediction": "DoS Attack"}
```

## 🖼️ Images
Include visuals like system architecture and sample alerts (add manually).

---
