import random


def triple_layer_sort(arr):
    if len(arr) > 1:
        one = random.choice(arr)
        two = random.choice(arr)
        three = random.choice(arr)
        print(one, two, three)

    min = []
    middle = []
    max = []
    for i in range(len(arr)):
        if arr[i] < one:
            min.append(arr[i])
        elif arr[i] < two:
            middle.append(arr[i])
        elif arr[i] < three | arr[i] > three:
            max.append(arr[i])

    print(min, middle, max)


def set_array(arr):
    if len(arr) > 1:
        triple_layer_sort(arr)


arr = [3, 4, 10, 38, 2, 6, 99]
set_array(arr)
# triple_layer_sort(arr)
