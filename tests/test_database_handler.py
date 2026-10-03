import database

from customer import Customer
from vehicle import Vehicle
from database import initialize_database
from database_handler import(
    save_customer_and_vehicle,
    get_all_customer_vehicles,
    delete_vehicle_by_license_plate,
    add_vehicle_to_existing_customer,
    update_customer_phone_by_license_plate,
    find_customer_by_license_plate,
    find_customer_by_vin,
    find_customers_by_first_name,
)
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


def test_delete_vehicle_keeps_customer(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    customer = Customer("Test", "Delete", "408-555-0002")
    vehicle = Vehicle(2024, "Honda", "Accord", "DELETEVIN123", "DELETE123")

    saved = save_customer_and_vehicle(customer, vehicle)
    assert saved is True
    delete_count = delete_vehicle_by_license_plate("DELETE123")

    assert delete_count == 1
    rows = get_all_customer_vehicles()
    assert len(rows) == 1
    row = rows[0]
    assert row[1] == "Test"
    assert row[4] is None

def test_add_vehicle_to_existing_customer(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    customer = Customer("Multi", "Vehicle", "408-555-0003")
    first_vehicle = Vehicle(2024, "Honda", "Civic", "FIRSTVIN123", "FIRST123")

    first_saved = save_customer_and_vehicle(customer, first_vehicle)
    assert first_saved is True

    rows = get_all_customer_vehicles()
    row = rows[0]
    customer_id = row[0]

    second_vehicle = Vehicle(2024, "Toyota", "Camry", "SECONDVIN123", "SECOND123")

    second_saved = add_vehicle_to_existing_customer(customer_id, second_vehicle)
    assert second_saved is True

    rows = get_all_customer_vehicles()
    assert len(rows) == 2
    assert rows[0][0] == customer_id
    assert rows[1][0] == customer_id

    vins = []
    for row in rows:
        vins.append(row[7])

    assert "FIRSTVIN123" in vins
    assert "SECONDVIN123" in vins


def test_duplicate_license_plate_rolls_back_customer(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    first_customer = Customer("Ingenium", "Labs", "408-555-0004")
    first_vehicle = Vehicle(2027, "Mercedes Benz", "GLE 63", "FIRSTUNIQUEVIN", "DUPLICATE123")

    first_saved = save_customer_and_vehicle(first_customer, first_vehicle)
    assert first_saved is True

    second_customer = Customer("Techne", "Labs", "408-555-0005")
    second_vehicle = Vehicle(2027, "BMW", "X5 M", "SECONDUNIQUEVIN", "DUPLICATE123")

    second_saved = save_customer_and_vehicle(second_customer, second_vehicle)
    assert second_saved is False

    rows = get_all_customer_vehicles()
    assert len(rows) == 1
    row = rows[0]
    assert row[8] == "DUPLICATE123"

def test_update_customer_phone_by_license_plate(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    first_customer = Customer("First", "Test", "408-555-0006")
    first_vehicle = Vehicle(2027, "Toyota", "Prius", "OLDPHONE123", "OLD123")

    first_saved = save_customer_and_vehicle(first_customer, first_vehicle)
    assert first_saved is True
    update_customer_phone_by_license_plate("OLD123", "408-555-0007")

    rows = get_all_customer_vehicles()
    row = rows[0]
    assert row[3] == "408-555-0007"

def test_update_customer_phone_with_unknown_plate(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    real_customer = Customer("First", "Test", "408-555-0007")
    real_vehicle = Vehicle(2027, "Toyota", "Prius", "OLDPHONE123", "OLD123")

    real_saved = save_customer_and_vehicle(real_customer, real_vehicle)
    assert real_saved is True
    update_customer_phone_by_license_plate("DOESNOTEXIST", "408-555-0008")

    rows = get_all_customer_vehicles()

    row = rows[0]
    assert row[3] == "408-555-0007"

def test_find_customer_by_license_plate(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    first_customer = Customer("First", "Test", "408-555-0007")
    first_vehicle = Vehicle(2027, "Toyota", "Prius", "OLDPHONE123", "OLD123")

    first_saved = save_customer_and_vehicle(first_customer, first_vehicle)
    assert first_saved is True

    result = find_customer_by_license_plate("OLD123")

    assert result[8] == "OLD123"


def test_find_customer_with_unknown_plate(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    first_customer = Customer("First", "Test", "408-555-0007")
    first_vehicle = Vehicle(2027, "Toyota", "Prius", "OLDPHONE123", "OLD123")

    saved = save_customer_and_vehicle(first_customer, first_vehicle)
    assert saved is True
    result = find_customer_by_license_plate("NOTREAL")
    assert result is None


def test_find_customer_by_vin(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    first_customer = Customer("First", "Test", "408-555-0007")
    first_vehicle = Vehicle(2027, "Toyota", "Prius", "OLDPHONE123", "OLD123")

    saved = save_customer_and_vehicle(first_customer, first_vehicle)
    assert saved is True
    result = find_customer_by_vin("OLDPHONE123")
    assert result[7] == "OLDPHONE123"


def test_find_customer_by_unknown_vin(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    first_customer = Customer("First", "Test", "408-555-0007")
    first_vehicle = Vehicle(2027, "Toyota", "Prius", "OLDPHONE123", "OLD123")

    saved = save_customer_and_vehicle(first_customer, first_vehicle)
    assert saved is True
    result = find_customer_by_vin("UNKNOWNVIN")
    assert result is None

def test_find_customers_by_first_name(tmp_path, monkeypatch):
    test_db = tmp_path / "test_collision_pros.db"
    monkeypatch.setattr(database, "DB_FILE", str(test_db))
    initialize_database()

    first_customer = Customer("John", "Wick", "408-911-9119")
    customer_one_vehicle = Vehicle(1967, "Ford", "Mustang", "BOOGEYMANVIN", "BGGYMAN")
    first_customer_saved = save_customer_and_vehicle(first_customer, customer_one_vehicle)
    assert first_customer_saved is True

    second_customer = Customer("John", "Deadpool", "669-911-1191")
    customer_two_vehicle = Vehicle(1967, "Chevrolet", "Camaro", "DEADPOOLVIN", "DEDPOOL")
    second_customer_saved = save_customer_and_vehicle(second_customer, customer_two_vehicle)
    assert second_customer_saved is True

    result = find_customers_by_first_name("John")

    assert len(result) == 2
    assert result[0][1] == "John"
    assert result[1][1] == "John"
    assert result[0][2] == "Wick"
    assert result[1][2] == "Deadpool"
