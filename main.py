from customer import Customer
from menu import show_welcome, menu_option
from file_handler import (
    save_customer, 
    display_saved_customers, 
    display_last_customer, 
    find_customer_by_name,
)
def main():
    show_welcome()

    selected_choice = menu_option()
    if selected_choice == 1:
        customer_name, customer_phone_number = get_customer_information()
        vehicle_vin, license_plate = get_vehicle_information()
        

        customer = Customer(
            customer_name,
            customer_phone_number,
            vehicle_vin,
            license_plate)
        
        save_customer(customer)
        customer.display_summary()

    elif selected_choice == 2:
        display_saved_customers()

    elif selected_choice == 3:
        display_last_customer()
    elif selected_choice == 4:
        find_customer_by_name()

    elif selected_choice == 5:
        print("Goodbye!")



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



if __name__ == "__main__":
    main()
