import database

from customer import Customer
from vehicle import Vehicle
from database import initialize_database
from database_handler import save_customer_and_vehicle, get_all_customer_vehicles

def test_save_customer_and_vehicle(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"

    monkeypatch.setattr(database, "DB_FILE", str(test_db))

    initialize_database()

    customer = Customer("Test", "Customer", "408-555-0000")
    vehicle = Vehicle(2024, "Honda", "Civic", "TESTVIN123", "TEST123")
    saved = save_customer_and_vehicle(customer, vehicle)
    assert saved is True

    rows = get_all_customer_vehicles()
    assert len(rows) == 1
    row = rows[0]
    assert row[1] == "Test"
    assert row[8] == "TEST123"


def test_duplicate_vin_rolls_back_customer(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    customer = Customer("Test", "Customer", "408-555-0000")
    vehicle = Vehicle(2024, "Honda", "Civic", "DUPLICATEVIN", "FIRST123")

    first_saved = save_customer_and_vehicle(customer, vehicle)
    assert first_saved is True
    second_customer = Customer("Duplicate", "Test", "408-555-0001")
    second_vehicle = Vehicle(2025, "Toyota", "TRD", "DUPLICATEVIN", "SECOND123")

    second_saved = save_customer_and_vehicle(second_customer, second_vehicle)
    assert second_saved is False

    rows = get_all_customer_vehicles()
    assert len(rows) == 1
    row = rows[0]
    assert row[1] == "Test"
    assert row[7] == "DUPLICATEVIN"
