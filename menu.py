def show_welcome():
    print("=" * 25)
    print("JR Collision Pros")
    print("Customer Intake System")
    print("=" * 25)

def menu_option():
    while True:
        print()
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. View Last Customer")
        print("4. Find Customer by First Name")
        print("5. Find Customer by Last Name")
        print("6. Find Customer by License Plate")
        print("7. Find Customer by VIN")
        print("8. Update Customer Phone Number")
        print("0. Exit")

        try:
            selected_choice = int(input("Choose an option: "))
            print()
            return selected_choice
        except ValueError:
            print()
            print("Invalid input. Please enter a number.")