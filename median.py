def median(numbers):
    good = sorted(numbers)
    lower_index = int(len(good)/2 - 1)
    upper_index = int(len(good)/2)
    middle_index = int(len(good)/2 - 0.5)
    if len(good) % 2 != 0:
        RIGHT = good[middle_index]
    elif len(good) % 2 == 0:
        RIGHT = (good[lower_index] + good[upper_index])/2
    return RIGHT
print(median([4, 5, 5, 4]))
