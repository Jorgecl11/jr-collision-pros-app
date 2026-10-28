from fastapi import FastAPI
from database_handler import get_all_vehicles
from pydantic import BaseModel

app = FastAPI()

class VehicleCreate(BaseModel):
    customer_id: int
    year: int
    make: str
    model: str
    vin: str
    license_plate: str

@app.get("/")
def home():
    return {"message": "Welcome to JR Collision Pros API"}

@app.get("/vehicles")
def get_vehicles():
    rows = get_all_vehicles()
    vehicles = []
    for row in rows:
        record = {
            "customer_id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "phone": row[3],
            "year": row[4],
            "make": row[5],
            "model": row[6],
            "vin": row[7],
            "license_plate": row[8],
        }
        vehicles.append(record)

    return {"vehicles": vehicles}

@app.post("/vehicles")
def create_vehicle(vehicle: VehicleCreate):
    return {
        "message": "Vehicle received",
        "customer_id": vehicle.customer_id,
        "year": vehicle.year,
        "make": vehicle.make,
        "model": vehicle.model,
        "vin": vehicle.vin,
        "license_plate": vehicle.license_plate
    }