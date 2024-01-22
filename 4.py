def max_sum_index(tuples):
    index, value = 0, sum(tuples[0])
    for ind, x in enumerate(tuples):
        temp = sum(x)
        if temp > value:
            value = temp
            index = ind

    return index


print(max_sum_index([(10, 20), (40, 32), (30, 25)]))
