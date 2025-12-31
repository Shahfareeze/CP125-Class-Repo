def count_bright_spots(pixels):
    i =1
    count = 0
    while i >= 5 :

        if pixels [i] > pixels [i + 1] and pixels [i] > pixels [i - 1]:
            result = "Bright Spot"
            count += 1
        else:
            result = "Not a bright spot"
    i += 1

    return count





pixels = [100, 120, 200, 150, 180, 160, 140]
print(count_bright_spots(pixels))
