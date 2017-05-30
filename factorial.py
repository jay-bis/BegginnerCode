def is_prime(x):
    total = x - 1
    wrong = 0
    right = 0
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x == 0:
        return False
    elif x < 0:
        return False
    else:
        while total >= 2:
            if x % total == 0:
                wrong = 1
                total = total - 1
            elif x % total != 0:
                right = 1
                total = total - 1
    if wrong == 1:
        return False
    elif wrong == 0:
        return True
print(is_prime(7))
