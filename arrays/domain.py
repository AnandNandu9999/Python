def print_array(arr, m, n):

    for i in range(m):
        for j in range(n):
            key = arr[i][j]
            l = r = 0
            brk = 0

            while l <= (i + j) + 1:
                while r <= (i + j) + 1:
                    if key >= arr[l][r]:
                        print(key)
                        r += 1
                    else:
                        brk = 1
                        break
                if brk == 1:
                    break
                else:
                    l += 1


arr = [[1, 3, 4]]
print_array(arr, 1, 3)