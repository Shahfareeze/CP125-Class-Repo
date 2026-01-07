
def analyze_performance(lap_times):
    first_laps = []
    second_laps = []

    for i in range (0,(len(lap_times))):
        if len(lap_times)%2 == 0:
            if i+1 <= len(lap_times) //2:
                first_laps.append(lap_times[i])
            else :
                second_laps.append(lap_times[i])
        else:
            if i+1 <= len(lap_times)//2:
                first_laps.append(lap_times[i])
            else :
                second_laps.append(lap_times[i])
    
    average_first = sum(first_laps)/len(first_laps)
    average_second = sum(second_laps)/len(second_laps)

    if average_second > average_first:
        return True
    else:
        return False



# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
