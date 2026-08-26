from database import initialize_database
from customer import Customer
from vehicle import Vehicle
from database_handler import (
    save_customer_and_vehicle,
    get_all_customer_vehicles,
    get_last_customer_vehicle,
    find_customers_by_first_name,
    find_customers_by_last_name,
    find_customer_by_license_plate,
    find_customer_by_vin,
    update_customer_phone_by_license_plate,
    )

from menu import show_welcome, menu_option

def main():
    initialize_database()
    show_welcome()
    while True:

        selected_choice = menu_option()
        if selected_choice == 1:
            first_name, last_name, phone_number = get_customer_information()
            year, make, model, vin, license_plate = get_vehicle_information()

            customer = Customer(
                first_name,
                last_name,
                phone_number
                )
            vehicle = Vehicle(
                year,
                make,
                model,
                vin,
                license_plate
                )
            saved = save_customer_and_vehicle(customer, vehicle)

            if saved:
                customer.display_summary()
                vehicle.display_summary()

        elif selected_choice == 2:
            rows = get_all_customer_vehicles()
            if rows:
                for row in rows:
                    display_customer_vehicle(row)
            else:
                print("No customers found.")

        elif selected_choice == 3:
            row = get_last_customer_vehicle()
            if row:
                display_customer_vehicle(row)
            else:
                print("No customers found.")

        elif selected_choice == 4:
            first_name = input("Enter first name to search: ").strip().title()
            rows = find_customers_by_first_name(first_name)
            if rows:
                for row in rows:
                    display_customer_vehicle(row)
            else:
                print("No customers found.")

        elif selected_choice == 5:
            last_name = input("Enter last name to search: ").strip().title()
            rows = find_customers_by_last_name(last_name)
            if rows:
                for row in rows:
                    display_customer_vehicle(row)
            else:
                print("No customers found.")


        elif selected_choice == 6:
            license_plate = input("Enter license plate to search: ").strip().upper()
            row = find_customer_by_license_plate(license_plate)
            if row:
                display_customer_vehicle(row)
            else:
                print("No customers found.")

        elif selected_choice == 7:
            vin = input("Enter Vin to search: ").strip().upper()
            row = find_customer_by_vin(vin)
            if row:
                display_customer_vehicle(row)
            else:
                print("No customers found.")

        elif selected_choice == 8:
            while True:
                license_plate = input("Enter license plate or 0 to return: ").strip().upper()

                if license_plate == "0":
                    break
                row = find_customer_by_license_plate(license_plate)

                if row:
                    while True:
                        new_phone = input("Enter new phone number or 0 to return to license plate search: ").strip()

                        if new_phone == "0":
                            break

                        phone_digits = new_phone.replace("-", "")

                        if phone_digits.isdigit() and len(phone_digits) == 10:
                            update_customer_phone_by_license_plate(license_plate, new_phone)
                            break
                        else:
                            print("Enter a valid 10-digit phone number, such as 408-555-1234.")
                else:
                    print("No customer found with that license plate.")


        elif selected_choice == 0:
            print("Goodbye!")
            break

        else:
            print("Invalid menu option!")



def get_customer_information():
    first_name = input("Enter first name: ").title()
    last_name = input("Enter last name: ").title()
    phone_number = input("Enter phone number: ")
    print(f"Welcome, {first_name} {last_name}")
    return first_name, last_name, phone_number

def get_vehicle_information():
    print("\nVehicle Information")
    print("-" * 20)
    year = int(input("Enter Year: "))
    make = input("Enter make: ").title()
    model = input("Enter model: ").title()
    vin = input("Enter vin number: ").upper()
    license_plate = input("Enter license plate: ").upper()
    print(f"VIN: {vin}")
    print(f"License Plate: {license_plate}")
    return year, make, model, vin, license_plate

def display_customer_vehicle(row):
    print(
        f"Customer ID: {row[0]} | "
        f"Name: {row[1]} {row[2]} | "
        f"Phone: {row[3]}\n"
        f"Vehicle: {row[4]} {row[5]} {row[6]} | "
        f"VIN: {row[7]} | "
        f"License Plate: {row[8]}"
    )



if __name__ == "__main__":
    main()
