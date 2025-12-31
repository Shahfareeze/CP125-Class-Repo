def count_bright_spots(pixels):
    count = 0
    i = 0 
    while i < len(pixels) - 1:
        if pixels [i]== pixels[0] or pixels[i] == pixels[-1]:
            count += 0
        elif pixels[i] > pixels[i - 1] and pixels[i] > pixels[i+1] :
            count += 1
        i += 1

    return count


data = [30, 20, 10]
print(count_bright_spots(data))
