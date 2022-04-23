def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [4, 1, 2, 3, 4, 9, 23, 5, 6]
bubble_sort(arr)
print(arr)