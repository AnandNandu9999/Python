def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


arr = [12, 11, 10, 6, 5, 5, 99, 1]
insertionSort(arr)
print(arr)