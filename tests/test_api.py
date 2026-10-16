import database
from database import initialize_database
from fastapi.testclient import TestClient
from api import app
from customer import Customer
from vehicle import Vehicle
from database_handler import save_customer_and_vehicle

def test_get_vehicles(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collisionpros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()
    client = TestClient(app)

    response = client.get("/vehicles")
    assert response.status_code == 200
    assert response.json()["vehicles"] == []

def test_get_vehicles_with_one_vehicle(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collisionpros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()
    client = TestClient(app)

    customer_1 = Customer("John", "Smith", "408-555-1234")
    vehicle_1 = Vehicle(2022, "Toyota", "Camry", "CAMRY123", "ABC123")
    saved_customer = save_customer_and_vehicle(customer_1, vehicle_1)
    assert saved_customer is True

    response = client.get("/vehicles")
    assert response.status_code == 200
    assert len(response.json()["vehicles"]) == 1
    assert response.json()["vehicles"][0]["make"] == "Toyota"
