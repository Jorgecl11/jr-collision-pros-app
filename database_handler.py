import sqlite3
from database import get_connection

def save_customer_and_vehicle(customer, vehicle):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO customers (first_name, last_name, phone) VALUES (?, ?, ?)",
            (customer.first_name, customer.last_name, customer.phone_number)
        )
        customer_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO vehicles (customer_id, year, make, model, vin, license_plate) VALUES (?, ?, ?, ?, ?, ?)",
            (customer_id, vehicle.year, vehicle.make, vehicle.model, vehicle.vin, vehicle.license_plate)
        )
        connection.commit()
        print("Customer and vehicle saved successfully.")
    except sqlite3.IntegrityError:
        print("Error: VIN or license plate already exists.")
    finally:
        connection.close()

def get_all_customer_vehicles():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT customers.id, customers.first_name, customers.last_name, customers.phone, vehicles.year, vehicles.make, vehicles.model, vehicles.vin, vehicles.license_plate 
        FROM customers
        LEFT JOIN vehicles
        ON customers.id = vehicles.customer_id
        """)
    rows = cursor.fetchall()
    connection.close()
    return rows

def get_last_customer_vehicle():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT customers.id, customers.first_name, customers.last_name, customers.phone, vehicles.year, vehicles.make, vehicles.model, vehicles.vin, vehicles.license_plate
    FROM customers
    LEFT JOIN vehicles
    ON customers.id = vehicles.customer_id
    ORDER BY customers.id DESC
    LIMIT 1
"""
    )
    row = cursor.fetchone()
    connection.close()
    return row

def find_customers_by_first_name(first_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT customers.id, customers.first_name, customers.last_name, customers.phone, vehicles.year, vehicles.make, vehicles.model, vehicles.vin, vehicles.license_plate
    FROM customers 
    LEFT JOIN vehicles
    ON customers.id = vehicles.customer_id
    WHERE customers.first_name = ?
    """,
    (first_name,)
    )
    rows = cursor.fetchall()
    connection.close()
    return rows

def find_customer_by_license_plate(license_plate):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
        SELECT customers.id, customers.first_name, customers.last_name, customers.phone, vehicles.year, vehicles.make, vehicles.model, vehicles.vin, vehicles.license_plate
        FROM customers 
        LEFT JOIN vehicles
        ON customers.id = vehicles.customer_id
        WHERE vehicles.license_plate = ?
        """,
        (license_plate,)
        )
        row = cursor.fetchone()
        connection.close()
        return row