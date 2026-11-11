from customer import Customer
from vehicle import Vehicle
from database_handler import save_customer_and_vehicle

def test_get_vehicles(client):
    response = client.get("/vehicles")
    assert response.status_code == 200
    assert response.json()["vehicles"] == []

def test_get_vehicles_with_one_vehicle(client):
    customer_1 = Customer("John", "Smith", "408-555-1234")
    vehicle_1 = Vehicle(2022, "Toyota", "Camry", "CAMRY123", "ABC123")
    saved_customer = save_customer_and_vehicle(customer_1, vehicle_1)
    assert saved_customer is True

    response = client.get("/vehicles")
    assert response.status_code == 200
    assert len(response.json()["vehicles"]) == 1
    assert response.json()["vehicles"][0]["make"] == "Toyota"
    assert response.json()["vehicles"][0]["model"] == "Camry"

def test_post_saved(client):
    customer_1 = Customer("John", "Smith", "408-555-1234")
    vehicle_1 = Vehicle(2022, "Toyota", "Camry", "CAMRY123", "ABC1559")
    saved = save_customer_and_vehicle(customer_1, vehicle_1)
    assert saved is True

    response = client.post("/vehicles", json={"customer_id": 1,"year": 2022, "make": "Toyota", "model": "Camry", "vin": "CAMRY15423", "license_plate": "ABC129"})
    assert response.status_code == 201
    response = client.get("/vehicles")

    vins = []
    for vehicle in response.json()["vehicles"]:
        vins.append(vehicle["vin"])
    assert "CAMRY15423" in vins

def test_post_customer_not_found(client):
    response = client.post("/vehicles", json={"customer_id": 999, "year": 2022, "make": "Toyota", "model": "Camry", "vin": "CAMRY15423", "license_plate": "ABC129"})
    assert response.status_code == 404
    response = client.get("/vehicles")

    vins = []
    for vehicle in response.json()["vehicles"]:
        vins.append(vehicle["vin"])
    assert "CAMRY15423" not in vins

def test_post_duplicate_vin(client):
    customer_1 = Customer("John", "Smith", "408-555-1234")
    vehicle_1 = Vehicle(2022, "Toyota", "Camry", "CAMRY123", "ABC1559")
    saved = save_customer_and_vehicle(customer_1, vehicle_1)
    assert saved is True

    response = client.post("/vehicles", json={"customer_id": 1,"year": 2022, "make": "Toyota", "model": "Camry", "vin": "CAMRY123", "license_plate": "ABC129"})
    assert response.status_code == 409
    response = client.get("/vehicles")
    assert len(response.json()["vehicles"]) == 1
    assert response.json()["vehicles"][0]["license_plate"] == "ABC1559"