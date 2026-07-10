def main():
    show_welcome()
    customer_name = get_customer_name()
    vehicle_vin, license_plate = get_vehicle_information()

    customer = {
        "name": customer_name,
        "vin": vehicle_vin,
        "license_plate": license_plate,

}
    
    repair_statuses = [
    "Estimate",
    "Estimate",
    "In Progress",
    "Completed",
    "Estimate",
    "Waiting for Parts",
    "Completed",
    "In Progress"
]
    display_repair_order_counts(repair_statuses)
    save_customer(customer)
    display_summary(customer)

def show_welcome():
    print("=" * 25)
    print("JR Collision Pros")
    print("Customer Intake System")
    print("=" * 25)

def get_customer_name():
    customer_name = input("Enter customer name: ").title()
    print(f"Welcome, {customer_name}")
    return customer_name

def get_vehicle_information():
    print("\nVehicle Information")
    print("-" * 20)
    vehicle_vin = input("Enter vin number: ").upper()
    license_plate = input("Enter license plate: ").upper()
    print(f"VIN: {vehicle_vin}")
    print(f"License Plate: {license_plate}")
    # return variables data
    return vehicle_vin, license_plate

def display_repair_order_counts(repair_statuses):
    repair_counts = {}
    print("=" * 25)
    print("Repair Statuses")
    print("=" * 25)
    for repair in repair_statuses:
        if repair in repair_counts:
            
            repair_counts[repair] += 1
        else:
            repair_counts[repair] = 1
    for key, value in repair_counts.items():
        print(f"{key}: {value}")

def save_customer(customer):
    with open("customers.txt", "a") as file:
        file.write(f"Name: {customer['name']}\n")
        file.write(f"VIN: {customer['vin']}\n")
        file.write(f"License Plate: {customer['license_plate']}\n")
        file.write("\n")

def display_summary(customer):
    print()
    print("=" * 25)
    print("Customer Summary")

    for key, value in customer.items():
        print(key.replace("_", " ").title() +':', value)
    print("=" * 25)


if __name__ == "__main__":
    main()
