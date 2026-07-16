def display_last_customer():
    with open("customers.txt", "r") as file:
        customers = file.readlines()
        last_customer = customers[-7:]
        for customer in last_customer:
            print(customer, end="")
    
display_last_customer()