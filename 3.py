def prime_nums(n: int) -> list:
    res = []
    check_nums = [2, 3, 5, 7]
    for number in range(2, n + 1):
        flag = False
        for check in check_nums:
            if check != number and number % check == 0:
                flag = True
                break
        if not flag:
            res += [number]

        flag = False

    return res


print('Prime numbers:', prime_nums(30))
