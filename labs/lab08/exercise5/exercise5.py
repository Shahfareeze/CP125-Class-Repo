# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv

def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.

    Args:
        input_file: path to sales CSV (product,quantity,price)
        output_file: path to output text file

    Returns:
        tuple: (total, average, highest, lowest)
    """
    # TODO: Implement this function
    f1 = open (input_file, "r", newline="")
    f2 = open (output_file, "w")

    sales = csv.reader(f1)
    next(sales)

    result = []
    for item in sales:
        revenue = float(item[1]) * float(item[2])
        result.append(revenue)

    total = sum(result)
    average = (sum(result)/len(result))
    highest = max(result)
    lowest = min(result)

    final = (total, average, highest, lowest)

    f2.write(f"Total Revenue: $ {total:.2f}\n")
    f2.write(f"Average Revenue: ${average:.2f}\n")
    f2.write(f"Highest Revenue: $ {highest:.2f}\n")
    f2.write(f"Lowest Revenue: $ {lowest:.2f}\n")

    f1.close()
    f2.close()


    return final


# Test your code here
result = summarize_sales("labs/lab08/exercise5/data/sales.csv", "labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
