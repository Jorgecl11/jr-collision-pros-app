import sqlite3

DB_FILE = "collisionpros.db"

def get_connection():
    connection = sqlite3.connect(DB_FILE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT
        );
""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        year INTEGER NOT NULL,
        make TEXT NOT NULL,
        model TEXT NOT NULL,
        vin TEXT UNIQUE,
        license_plate TEXT UNIQUE,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
    
""")
    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()