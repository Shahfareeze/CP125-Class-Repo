# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    round_trip_km = one_way_km*2
    round_trip_cost = (round_trip_km / km_per_liter ) * price_per_liter
    if round_trip_cost <= budget :
        return True
    else:
        return False
    

# Test your code here

print("Testing Road Trip Budgeter...")
result = is_budget_sufficient(4, 0.5, 1.5, 10 )
if result:
    print ("You have enough money")
else:
    print ("Not enough money")