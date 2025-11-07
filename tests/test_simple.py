from fastapi.testclient import TestClient
from api.create_item import app

client = TestClient(app=app)

def test_create_item():
    response = client.post("/items_test", json={"name": "new_nana"})
    assert response.status_code == 200