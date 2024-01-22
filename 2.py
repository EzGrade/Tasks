def sec_smallest(numbers: list) -> int:
    first, second = float("inf"), float("inf")
    for number in numbers:
        if number < first:
            first = number

        if second > number > first:
            second = number

    return second


print('Sec_smallest:', sec_smallest([1, 2, -8, -8, -2, 0]))
