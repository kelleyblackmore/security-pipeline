from app.app import app


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"


def test_echo():
    client = app.test_client()
    response = client.post("/echo", json={"ping": "pong"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["received"]["ping"] == "pong"
