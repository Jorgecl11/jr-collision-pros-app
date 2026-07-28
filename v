[1mdiff --git a/main.py b/main.py[m
[1mindex c3efa71..06128bc 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -1,3 +1,23 @@[m
[32m+[m[32mclass Customer:[m
[32m+[m
[32m+[m[32m    def __init__(self, name, phone_number, vin, license_plate):[m
[32m+[m[32m        self.name = name[m
[32m+[m[32m        self.phone_number = phone_number[m
[32m+[m[32m        self.vin = vin[m
[32m+[m[32m        self.license_plate = license_plate[m
[32m+[m
[32m+[m[32m    def display_summary(self):[m
[32m+[m[32m        print()[m
[32m+[m[32m        print("=" * 25)[m
[32m+[m[32m        print("Customer Summary")[m
[32m+[m[32m        print(f"Name: {self.name.title()}")[m
[32m+[m[32m        print(f"Phone number: {self.phone_number}")[m
[32m+[m[32m        print(f"VIN: {self.vin.upper()}")[m
[32m+[m[32m        print(f"License Plate: {self.license_plate.upper()}")[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
 def main():[m
     show_welcome()[m
 [m
[36m@@ -7,13 +27,14 @@[m [mdef main():[m
         vehicle_vin, license_plate = get_vehicle_information()[m
         [m
 [m
[31m-        customer = {[m
[31m-            "name": customer_name,[m
[31m-            "phone": customer_phone_number,[m
[31m-            "vin": vehicle_vin,[m
[31m-            "license_plate": license_plate,[m
[31m-        }[m
[32m+[m[32m        customer = Customer([m
[32m+[m[32m            customer_name,[m
[32m+[m[32m            customer_phone_number,[m
[32m+[m[32m            vehicle_vin,[m
[32m+[m[32m            license_plate)[m
[32m+[m[41m        [m
         save_customer(customer)[m
[32m+[m[32m        customer.display_summary()[m
 [m
     elif selected_choice == 2:[m
         display_saved_customers()[m
[36m@@ -24,26 +45,6 @@[m [mdef main():[m
     elif selected_choice == 4:[m
         print("Goodbye!")[m
 [m
[31m-[m
[31m-     [m
[31m-    [m
[31m-    # repair_statuses = [[m
[31m-    # "Estimate",[m
[31m-    # "Estimate",[m
[31m-    # "In Progress",[m
[31m-    # "Completed",[m
[31m-    # "Estimate",[m
[31m-    # "Waiting for Parts",[m
[31m-    # "Completed",[m
[31m-    # "In Progress"[m
[31m-    # ][m
[31m-    # display_repair_order_counts(repair_statuses)[m
[31m-    [m
[31m-    # find_customer_by_name()[m
[31m-[m
[31m-    [m
[31m-    [m
[31m-[m
 def show_welcome():[m
     print("=" * 25)[m
     print("JR Collision Pros")[m
[36m@@ -92,20 +93,12 @@[m [mdef display_repair_order_counts(repair_statuses):[m
 def save_customer(customer):[m
     with open("customers.txt", "a") as file:[m
         file.write("=" * 25 + "\n")[m
[31m-        file.write(f"Name: {customer['name']}\n")[m
[31m-        file.write(f"Phone: {customer['phone']}\n")[m
[31m-        file.write(f"VIN: {customer['vin']}\n")[m
[31m-        file.write(f"License Plate: {customer['license_plate']}\n")[m
[32m+[m[32m        file.write(f"Name: {customer.name}\n")[m
[32m+[m[32m        file.write(f"Phone: {customer.phone_number}\n")[m
[32m+[m[32m        file.write(f"VIN: {customer.vin}\n")[m
[32m+[m[32m        file.write(f"License Plate: {customer.license_plate}\n")[m
         file.write("=" * 25 + "\n\n")[m
 [m
[31m-def display_summary(customer):[m
[31m-    print()[m
[31m-    print("=" * 25)[m
[31m-    print("Customer Summary")[m
[31m-[m
[31m-    for key, value in customer.items():[m
[31m-        print(key.replace("_", " ").title() +':', value)[m
[31m-    print("=" * 25)[m
 [m
 [m
 def display_saved_customers():[m
