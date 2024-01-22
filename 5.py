def gcd(x, y):
    # Slowest way
    for num in range(min([x, y]), 1, -1):
        if x % num == 0 and y % num == 0:
            return num


print(gcd(160, 180))
