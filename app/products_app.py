#from IPython import embed
import csv

products = []

products_csv = "data/products.csv"
headers = ["id", "name", "aisle", "department", "price"] # for "Further Exploration" use: ["product_id", "product_name", "aisle_id", "aisle_name", "department_id", "department_name", "price"]
user_input_headers = [header for header in headers if header != "id"] # don't prompt the user for the product_id

def get_product_id(product): return int(product["id"])

def auto_incremented_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

#
# READ PRODUCTS FROM FILE
#

with open(products_csv, "r",newline="") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))

#
# HANDLE USER INPUT
#

def list_products():
    print("LISTING PRODUCTS HERE")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("READING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product)

def create_product():
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product = {"id": auto_incremented_id() }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT HERE", product)

def update_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

def destroy_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

menu = """

----------------------------------------------------------------------------------------
PRODUCTS APPLICATION
----------------------------------------------------------------------------------------
Hi {0}, welcome to the Products Application! Enjoy and have a great day!

There are {1} products in the database. Here is a list of the available operations: \n

OPERATION  | DESCRIPTION
-----------|---------------------------------------------------
'List'     | Display a list of product identifiers and names.
'Show'     | Show information about a product.
'Create'   | Add a new product.
'Update'   | Edit an existing product.
'Destroy'  | Delete an existing product.

Please select an operation: """.format("@jrn223", len(products)) # end of multi- line string. also using string interpolation

crud_operation = input(menu)

if crud_operation.title() == "List":
    list_products()
elif crud_operation.title() == "Show":
    show_product()
elif crud_operation.title() == "Create":
    create_product()
elif crud_operation.title() == "Update":
    update_product()
elif crud_operation.title() == "Destroy":
    destroy_product()
else:
    print("OOPS SORRY. PLEASE TRY AGAIN.")

#
# WRITE PRODUCTS TO FILE
#

with open(products_csv, "w",newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

    for product in products:
        writer.writerow(product)

# Spent about 10 hours trying to get this code to work but was unable to do it so am picking up code you shared
# import csv
#
# csv_file_path = "data\products.csv"
#
# products = []
#
# def handler():
#     user_input = input ("Please select an operation:")
#
#     if user_input == "List":
#         list_products()
#     elif user_input == "Show":
#         while (True):
#             if show():
#                 break
#             else:
#                 print("Product Not Found")
#     elif user_input == "Create":
#         create()
#     elif user_input == "Update":
#         while (True):
#             if update():
#                 break
#             else:
#                 print("Product Not Found")
#     elif user_input == "Destroy":
#         while (True):
#             if destroy():
#                 break
#             else:
#                 print("Product Not Found")
#     else:
#         print("OOPS. UNRECOGNIZED OPERATION. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
#
# def list_products():
#     print("List")
#     with open(csv_file_path, "r") as csv_file:
#         reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
#         for row in reader:
#             print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
#
# def show():
#     found = False
#     print("Show")
#     show_input = input ("OK. Please specify the product's identifier:")
#     with open(csv_file_path, "r") as csv_file:
#         reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
#
#         for row in reader:
#             if show_input == row["id"]:
#                 print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
#                 found = True
#     return found
#
# def create():
#     print("Create")
#     print("OK. Please specify the product's information ...")
#     new_id = 1
#     with open(csv_file_path, "r") as csv_file:
#         reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
#         for row in reader:
#             new_id = int(row["id"]) + 1
#     new_name = input ("name:")
#     new_aisle = input ("aisle:")
#     new_department = input ("department:")
#     new_price = input ("price:")
#     print("CREATING A PRODUCT HERE!")
#     with open(csv_file_path, "a",newline="") as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
#         writer.writerow({"id": new_id, "name": new_name, "aisle": new_aisle, "department": new_department, "price": new_price})
#
# def update():
#     print("Update")
#     product_number = input ("OK. Please specify the product's identifier:")
#     print("OK. Please specify the product's information ...")
#     with open(csv_file_path, "r") as csv_file:
#         reader = csv.DictReader(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
#         # writer = csv.writer(open(csv_file_path, "w"))
#         # writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
#         for row in reader:
#             print(row['id'])
#             if row ["id"] == int(product_number):
#                 update_name = input("Change name from '" + row["name"] + "' to:")
#                 update_aisle = input("Change name from '" + row["aisle"] + "' to:")
#                 update_department = input("Change name from '" + row["department"] + "' to:")
#                 update_price = input("Change name from '" + row["price"] + "' to:")
#                 writer.writerow({'name': update_name, 'aisle': update_aisle, 'department': update_department, 'price': update_price})
#                 print("UPDATING A PRODUCT HERE!")
#
# def destroy():
#     print("Destroy")
#     destroy_product = input("OK. Please specify the product's identifier:")
#     load_products()
#     product = ""
#     for item in products:
#         if item['id'] == int(destory_product):
#             product = item
#     # product = [p for p in products if p["id"] == destroy_product][0]
#     if product:
#         print("DESTROYING A PRODUCT HERE!", product)
#         del products[products.index(product)]
#         return True
#     else:
#         print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", destroy_product)
#         return False
#
# def load_products():
#     with open(csv_file_path, "r") as csv_file:
#         reader = csv.DictReader(csv_file)
#         for ordered_dict in reader:
#             products.append(dict(ordered_dict))
#     print(products)
#
# handler()
#
# with open(csv_file_path, "w") as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
#     writer.writeheader()
#
#     for product in products:
#         writer.writerow(product)
