def save_customer(customer):
    with open("customers.txt", "a") as file:
        file.write("=" * 25 + "\n")
        file.write(f"Name: {customer.name}\n")
        file.write(f"Phone: {customer.phone_number}\n")
        file.write(f"VIN: {customer.vin}\n")
        file.write(f"License Plate: {customer.license_plate}\n")
        file.write("=" * 25 + "\n\n")



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