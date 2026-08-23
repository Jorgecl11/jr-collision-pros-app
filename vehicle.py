class Vehicle:
    def __init__(self, year, make, model, vin, license_plate):
        self.year = year
        self.make = make
        self.model = model
        self.vin = vin
        self.license_plate = license_plate

    def display_summary(self):
        print()
        print("=" * 25)
        print("Vehicle Summary")
        print(f"Year: {self.year}")
        print(f"Make: {self.make.title()}")
        print(f"Model: {self.model.title()}")
        print(f"VIN: {self.vin.upper()}")
        print(f"License Plate: {self.license_plate.upper()}")