def square_root_with_map_fun(arr):
    type_of_map = map(lambda x: x**2, arr)
    type_of_lambda = lambda x: x ** 2, arr
    print(type(type_of_map))  # <class 'map'>
    print(type_of_map)  # <map object at 0x0147EBF8>
    print(type(type_of_lambda))  # <class 'tuple'>
    print(list(type_of_lambda))  # [<function square_root_with_map_fun.<locals>.<lambda> at 0x0160D2F8>, [1, 2, 3, 4,
    # 5]]
    return list(map(lambda x: x**2, arr))  # [1, 4, 9, 16, 25]


def square_root_without_map_fun(arr):
    out = []
    for i in range(len(arr)):
        out.append(arr[i] * arr[i])
    return out


arr = [1, 2, 3, 4, 5]
print(square_root_with_map_fun(arr))
print(square_root_without_map_fun(arr))