
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.

    """

    if len(times) == 0:
        return []
    mean = sum(times)/(len(times))
    variance = sum((value - mean)**2 for value in times)/ (len(times))
    std_dev = variance**0.5
    upper_limit = mean + std_dev
    new_times = []
    for i in times:
        if i <= upper_limit:
            new_times.append(i)


    new_times.sort()
    return new_times


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
