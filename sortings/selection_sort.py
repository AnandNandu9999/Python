def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        # swap min_index and j
        arr[i], arr[min_index] = arr[min_index], arr[i]


import time

start = time.time()
arr = [64, 45, 23, 1, 35, 99]
selectionSort(arr)
print(arr)
print((time.time() - start) * 1000)

