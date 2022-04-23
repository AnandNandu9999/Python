def func_with_filter(arr):
    print(type(filter(lambda x: x > 3, arr)))
    return list(filter(lambda x: x > 3, arr))


def func_without_filter(arr):
    out = []
    for i in range(len(arr)):
        if arr[i] > 3:
            out.append(arr[i])
        else:
            continue
    return out


arr = [1, 2, 3, 4, 5]
print(func_with_filter(arr))
print(func_without_filter(arr))
