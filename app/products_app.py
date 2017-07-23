import csv

csv_file_path = "data\products.csv"

products = []

print("----------------------------------------------------------------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------------------------------------------------------------")
print("Hi jrn223, welcome to the Products Application! Enjoy and have a great day!")

print("\n \nThere are 20 products in the database. Here is a list of the available operations: \n \n")

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
    print("Show")
    print("OK. Please specify the product's information ...")
    input ("name:")
    input ("aisle:")
    input ("department:")
    input ("price:")
    print("CREATING A PRODUCT HERE!")
else:
    print("OOPS. UNRECOGNIZED OPERATION. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
