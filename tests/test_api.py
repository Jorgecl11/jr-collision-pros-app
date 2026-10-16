import database
from database import initialize_database
from fastapi.testclient import TestClient
from api import app

def test_get_vehicles(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collisionpros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()
    client = TestClient(app)

    response = client.get("/vehicles")
    assert response.status_code == 200
    assert response.json()["vehicles"] == []