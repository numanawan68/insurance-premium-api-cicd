from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_predict():
    response = client.post("/predict", json={
        "age": 35,
        "weight": 70,
        "height": 1.75,
        "income_lpa": 8.0,
        "smoker": True,
        "city": "Istanbul",
        "occupation": "retired"
    })

    assert response.status_code == 200

    data = response.json()["response"]

    assert "predicted_category" in data
    assert "confidence" in data
    assert "class_probs" in data

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200
def test_predict_invalid_height():
    response = client.post("/predict", json={
        "age": 35,
        "weight": 70,
        "height": 175,
        "income_lpa": 8.0,
        "smoker": True,
        "city": "Istanbul",
        "occupation": "retired"
    })

    assert response.status_code == 422