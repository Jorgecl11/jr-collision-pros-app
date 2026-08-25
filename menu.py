def show_welcome():
    print("=" * 25)
    print("JR Collision Pros")
    print("Customer Intake System")
    print("=" * 25)

def menu_option():
    print("1. Add Customer")
    print("2. View All Customers")
    print("3. View Last Customer")
    print("4. Find Customer by First Name")
    print("5. Find Customer by Last Name")
    print("6. Find Customer by License Plate")
    print("7. Find customer by VIN")
    print("0. Exit")

    selected_choice = int(input("Choose an option: "))
    return selected_choice
