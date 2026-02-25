# SHAHFAREEZE BIN RAMLEE
# Create a program that accepts 5 integer input values from the user and is stored in a list. 

def sort_number(list_number):
    return list_number.sort()

def calculate_sum_of_number(list_number):
    return sum(list_number)

def find_largest_number(list_number):
    return max(list_number)

def input_from_user(list_number):
    i=1
    while i < 6:
        number = int(input(f"Enter number {i}:"))
        i = i + 1
        list_number.append(number)

    ascending_order = sorted(list_number)
    sum_all_number = calculate_sum_of_number(list_number)
    largest = find_largest_number(list_number)


    print(f"Number in ascending order: {ascending_order}")
    print(f"Sum of all number: {sum_all_number}")
    print(f"Largest number: {largest}")
    print("=== Code Execution Succesful ===")

list_number = []
input_from_user(list_number)
