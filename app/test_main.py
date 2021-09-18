from fastapi.testclient import TestClient
from app.main import app, filter_pairs

client = TestClient(app)


def test_main_resource():
    response_auth = client.get("/")
    assert response_auth.status_code == 200


def test_filter_pairs():
    filter_endpoint = "/pairs/filter/?correlation_type=pearson&bigger_than=0.9&smaller_than=None&order_by=DESC&limit=1"
    response_auth = client.get(filter_endpoint)
    assert response_auth.status_code == 200
