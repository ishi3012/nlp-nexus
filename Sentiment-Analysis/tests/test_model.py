import requests

def test_predict_sentiment():
    url = 'http://localhost:5000/predict'
    response = requests.post(url, json={'text': 'I love this product!'})
    assert response.status_code == 200
    assert 'sentiment' in response.json()
