def main():
    show_welcome()

    selected_choice = menu_option()
    if selected_choice == 1:
        customer_name, customer_phone_number = get_customer_information()
        vehicle_vin, license_plate = get_vehicle_information()
        

        customer = {
            "name": customer_name,
            "phone": customer_phone_number,
            "vin": vehicle_vin,
            "license_plate": license_plate,
        }
        save_customer(customer)

    elif selected_choice == 2:
        display_saved_customers()

    elif selected_choice == 3:
        display_last_customer()

    elif selected_choice == 4:
        print("Goodbye!")


     
    
    # repair_statuses = [
    # "Estimate",
    # "Estimate",
    # "In Progress",
    # "Completed",
    # "Estimate",
    # "Waiting for Parts",
    # "Completed",
    # "In Progress"
    # ]
    # display_repair_order_counts(repair_statuses)
    
    # find_customer_by_name()

    
    

def show_welcome():
    print("=" * 25)
    print("JR Collision Pros")
    print("Customer Intake System")
    print("=" * 25)

def menu_option():
    print("1. Add Customer")
    print("2. View All Customers")
    print("3. View Last Customer")
    print("4. Exit")

    selected_choice = int(input("Choose an option: "))
    return selected_choice


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

def find_customer_by_name():
    customer_name = input("Enter customer name to search: ").title()
    found_customer = False

    with open("customers.txt", "r") as file:
        for line in file:
            if customer_name in line:
                found_customer = True

            if found_customer == True and line.strip() != "=" *25:
                print(line)
            else:
                found_customer = False

def display_last_customer():

    with open("customers.txt", "r") as file:
        customers = file.readlines()
        last_customer = customers[-7:]
        for customer in last_customer:
            print(customer, end="")

if __name__ == "__main__":
    main()
