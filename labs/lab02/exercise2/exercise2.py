# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    total_tent = participants // tent_capacity 
    if participants%tent_capacity == 0:
        total_tent = total_tent
    else:
        total_tent += 1

    total_meal_price= participants * meal_price
    total_budget = (total_tent * tent_price) + (total_meal_price)
    return total_budget

# Test your code here

print("Testing Camping Logistics...")
result = calculate_event_cost(10, 5, 10, 5)
print (result)
