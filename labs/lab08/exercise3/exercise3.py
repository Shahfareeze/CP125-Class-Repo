# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function
    f1 = open (products_file, "r", newline= "")
    f2 = open (order_file, "r", newline= "")
    f3 = open (output_file, "w", newline="")

    product = csv.reader(f1)
    order = csv.reader(f2)
    next(product)
    product_item = {}
    for item in product:
        product_item[item[0]] = item[2]

    next(order)
    output = csv.writer(f3)
    output.writerow(["product_id","total_cost"])
    grand_total = 0
    for element in order:
        result = float(element[1]) * float(product_item[element[0]])
        output.writerow([element[0], f"{result:.2f}"])
        grand_total += result


    return grand_total


# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
