class Customer:

    def __init__(self, name, phone_number, vin, license_plate):
        self.name = name
        self.phone_number = phone_number
        self.vin = vin
        self.license_plate = license_plate

    def display_summary(self):
        print()
        print("=" * 25)
        print("Customer Summary")
        print(f"Name: {self.name.title()}")
        print(f"Phone number: {self.phone_number}")
        print(f"VIN: {self.vin.upper()}")
        print(f"License Plate: {self.license_plate.upper()}")
