def main():
    show_welcome()
    customer_name = get_customer_name()
    vehicle_vin, license_plate = get_vehicle_information()
    customer = {
    "name": customer_name,
    "vin": vehicle_vin,
    "license_plate": license_plate,

}
    display_summary(customer)

def show_welcome():
    print("=" * 25)
    print("JR Collision Pros")
    print("Customer Intake System")
    print("=" * 25)

def get_customer_name():
    customer_name = input("Enter customer name: ").title()
    print(f"Welcome, {customer_name}")
    print(f"Name Length: {len(customer_name)}")
    print(f"First Letter: {customer_name[0]}")
    print(f"Last Letter: {customer_name[-1]}")
    return customer_name

def get_vehicle_information():
    print("\nVehicle Information")
    print("-" * 20)
    vehicle_vin = input("Enter vin number: ").upper()
    license_plate = input("Enter license plate: ").upper()
    print(f"VIN: {vehicle_vin}")
    print(f"VIN Length: {len(vehicle_vin)}")
    print(f"First Character: {vehicle_vin[0]}\n")
    # VINs and license plates are stored as strings because they identify a vehicle.
    # We compare and display them rather than perform mathematical calculations.
    print(f"License Plate: {license_plate}")
    print(f"Plate Length: {len(license_plate)}")

    # return variables data
    return vehicle_vin, license_plate

def display_summary(customer):
    print("=" * 25)
    print("Customer Summary")
    print("=" * 25)
    print(f"Customer: {customer['name']}\n")

    print(f"VIN: {customer['vin']}")
    print(f"License Plate: {customer['license_plate']}\n")

    print("\nThank you for choosing\nJR Collision Pros!")



if __name__ == "__main__":
    main()
