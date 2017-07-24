import csv

csv_file_path = "data\products.csv"

products = []

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

print("----------------------------------------------------------------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------------------------------------------------------------")
print("Hi jrn223, welcome to the Products Application! Enjoy and have a great day!")

with open(csv_file_path, "r") as csv_file:
    number_products = sum(1 for row in csv_file) - 1
    print("\n \nThere are " + str(number_products) + " products in the database. Here is a list of the available operations: \n \n")

print("OPERATION  | DESCRIPTION")
print("-----------|---------------------------------------------------")
print("'List'     | Display a list of product identifiers and names.")
print("'Show'     | Show information about a product.")
print("'Create'   | Add a new product.")
print("'Update'   | Edit an existing product.")
print("'Destroy'  | Delete an existing product. \n \n")

user_input = input ("Please select an operation:")

if user_input == "List":
    print("List")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
elif user_input == "Show":
    while (True):
        if show():
            break
        else:
            print("Product Not Found")

elif user_input == "Update":
    print("Update")
    print("OK. Please specify the product's information ...")
    input ("name:")
    input ("aisle:")
    input ("department:")
    input ("price:")
    print("CREATING A PRODUCT HERE!")
elif user_input == "Destroy":
    print("Destroy")
else:
    print("OOPS. UNRECOGNIZED OPERATION. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
