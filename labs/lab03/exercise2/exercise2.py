def find_station(stations, name):
    if name not in stations :
        return None
    for i in range (len(stations)):
        if stations[i] == name:
            return i
        

def count_stops(stations, start, stop):
    
    index_start = find_station (stations, start)
    index_stop = find_station (stations, stop)
    if index_start == None or index_stop == None:
        return -1
    count = index_stop - index_start
    count = abs(count)
    return count


Stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
result = find_station(Stations, "Unknown")
print (result)
