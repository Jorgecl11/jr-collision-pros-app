class Customer:

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number


    def display_summary(self):
        print()
        print("=" * 25)
        print("Customer Summary")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Phone number: {self.phone_number}")
