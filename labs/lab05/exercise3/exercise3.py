
def find_bottleneck_index(traceroute):
    """
    Find the index of the hop where the largest latency jump begins.
    """

    index = 0 
    largest_hops = 0 

    for i in range (1,(len(traceroute))):
        hops1, jumps1 = traceroute[i]
        hops2, jumps2 = traceroute[i-1]

        difference_hops = jumps1 - jumps2
        if difference_hops > largest_hops:
            largest_hops = difference_hops
            index = i-1

        
    return index 




# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
