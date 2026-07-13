def main():
    show_welcome()
    customer_name, customer_phone_number = get_customer_information()
    vehicle_vin, license_plate = get_vehicle_information()

    customer = {
        "name": customer_name,
        "phone": customer_phone_number,
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
    display_saved_customers()

def show_welcome():
    print("=" * 25)
    print("JR Collision Pros")
    print("Customer Intake System")
    print("=" * 25)

def get_customer_information():
    customer_name = input("Enter customer name: ").title()
    customer_phone_number = input("Enter phone number: ")
    print(f"Welcome, {customer_name}")
    return customer_name, customer_phone_number

def get_vehicle_information():
    print("\nVehicle Information")
    print("-" * 20)
    vehicle_vin = input("Enter vin number: ").upper()
    license_plate = input("Enter license plate: ").upper()
    print(f"VIN: {vehicle_vin}")
    print(f"License Plate: {license_plate}")
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
        file.write("=" * 25 + "\n")
        file.write(f"Name: {customer['name']}\n")
        file.write(f"Phone: {customer['phone']}\n")
        file.write(f"VIN: {customer['vin']}\n")
        file.write(f"License Plate: {customer['license_plate']}\n")
        file.write("=" * 25 + "\n\n")

def display_summary(customer):
    print()
    print("=" * 25)
    print("Customer Summary")

    for key, value in customer.items():
        print(key.replace("_", " ").title() +':', value)
    print("=" * 25)


def display_saved_customers():
    print()
    print("=" * 25)
    print("Saved Customers")
    print("=" * 25)

    with open("customers.txt", "r") as file:
        for line in file:
            print(line, end="")


if __name__ == "__main__":
    main()
