def recursive_list_sum(data_list: list):
    if not data_list:
        return 0
    if isinstance(data_list[0], int):
        return data_list[0] + recursive_list_sum(data_list[1:])
    else:
        return sum(data_list[0]) + recursive_list_sum(data_list[1:])


print('The sum of a list is ', recursive_list_sum([1, 2, [3, 4], [5, 6], [7, 8, 9]]))
