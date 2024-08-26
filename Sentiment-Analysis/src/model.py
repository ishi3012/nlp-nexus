import joblib

def load_model():
    return joblib.load('models/saved-models/sentiment_model.pkl')

def predict_sentiment(model, text):
    # Implement sentiment prediction logic
    prediction = model.predict([text])
    return prediction[0]
