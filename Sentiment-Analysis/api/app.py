from flask import Flask, request, jsonify
from src.model import load_model, predict_sentiment

app = Flask(__name__)
model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    prediction = predict_sentiment(model, text)
    return jsonify({'sentiment': prediction})

if __name__ == '__main__':
    app.run(debug=True)
