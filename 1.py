def str_to_dict(s: str) -> dict:
    result = {}
    for char in s:
        if char not in result:
            result[char] = s.count(char)
    return result


print('Str to dict:', str_to_dict('dataroot_university'))
