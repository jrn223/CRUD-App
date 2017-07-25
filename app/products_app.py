import csv

csv_file_path = "data\products.csv"

products = []

print("----------------------------------------------------------------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------------------------------------------------------------")
print("Hi, welcome to the Products Application! Enjoy and have a great day!")

print("There are {1} products in the database. Here is a list of the available operations: \n")

print("OPERATION  | DESCRIPTION")
print("-----------|---------------------------------------------------")
print("'List'     | Display a list of product identifiers and names.")
print("'Show'     | Show information about a product.")
print("'Create'   | Add a new product.")
print("'Update'   | Edit an existing product.")
print("'Destroy'  | Delete an existing product.")

def handler():
     user_input = input ("Please select an operation:")

     if user_input == "List":
         list_products()
     elif user_input == "Show":
         while (True):
             if show():
                 break
             else:
                 print("Product Not Found")
     elif user_input == "Create":
         create()
     elif user_input == "Update":
         while (True):
             if update():
                 break
             else:
                 print("Product Not Found")
     elif user_input == "Destroy":
         while (True):
             if destroy():
                 break
             else:
                 print("Product Not Found")
     else:
         print("OOPS. UNRECOGNIZED OPERATION. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

def list_products():
     print("List")
     with open(csv_file_path, "r") as csv_file:
         reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
         for row in reader:
             print(row["id"], row["name"], row["aisle"], row["department"], row["price"])

def show():
     found = False
     print("Show")
     show_input = input ("OK. Please specify the product's identifier:")
     with open(csv_file_path, "r") as csv_file:
         reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)

         for row in reader:
             if show_input == row["id"]:
                 print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
                 found = True
                 return found

def create():
     print("Create")
     print("OK. Please specify the product's information ...")
     new_id = 1
     with open(csv_file_path, "r") as csv_file:
         reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
         for row in reader:
             new_id = int(row["id"]) + 1
     new_name = input ("name:")
     new_aisle = input ("aisle:")
     new_department = input ("department:")
     new_price = input ("price:")
     print("CREATING A PRODUCT HERE!")
     with open(csv_file_path, "a",newline="") as csv_file:
         writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
         writer.writerow({"id": new_id, "name": new_name, "aisle": new_aisle, "department": new_department, "price": new_price})

def update():
     print("Update")
     product_number = input ("OK. Please specify the product's identifier:")
     print("OK. Please specify the product's information ...")
     with open(csv_file_path, "r") as csv_file:
         reader = csv.DictReader(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
         writer = csv.writer(open(csv_file_path, "w"))
         writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
         for row in reader:
             print(row['id'])
             if row ["id"] == int(product_number):
                 update_name = input("Change name from '" + row["name"] + "' to:")
                 update_aisle = input("Change name from '" + row["aisle"] + "' to:")
                 update_department = input("Change name from '" + row["department"] + "' to:")
                 update_price = input("Change name from '" + row["price"] + "' to:")
                 writer.writerow({'name': update_name, 'aisle': update_aisle, 'department': update_department, 'price': update_price})
                 print("UPDATING A PRODUCT HERE!")

def destroy():
     print("Destroy")
     destroy_product = input("OK. Please specify the product's identifier:")
     load_products()
     product = ""
     for item in products:
         if item['id'] == int(destory_product):
             product = item
     # product = [p for p in products if p["id"] == destroy_product][0]
     if product:
         print("DESTROYING A PRODUCT HERE!", product)
         del products[products.index(product)]
         return True
     else:
         print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", destroy_product)
         return False
