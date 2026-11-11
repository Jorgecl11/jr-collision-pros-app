import pytest
import database
from database import initialize_database
from fastapi.testclient import TestClient
from api import app

@pytest.fixture
def client(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collisionpros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()
    return TestClient(app)