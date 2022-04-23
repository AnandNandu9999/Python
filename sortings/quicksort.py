def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end


def quickSort(low, high, arr):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(low, pi - 1, arr)
        quickSort(pi + 1, high, arr)


arr = [3, 11, 1, 50, 60, 90, 2, 5]
quickSort(0, len(arr) - 1, arr)
print(arr)