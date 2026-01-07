

def find_momentum_days(prices):
    previous_change = 100 
    momemtum_day = []
    for i in range (1,(len(prices))):
        if prices[i]-prices[i-1] > previous_change:
            momemtum_day.append(i)

        previous_change = prices[i]-prices[i-1]

    return momemtum_day



# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]
