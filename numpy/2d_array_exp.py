import numpy as np

data = np.array([(11, 12, 13), (4, 5, 6), (7, 8, 9)])

# prints the no. of dimensions
# prints the no. of rows and columns
# print(data.size, data.shape)

# prints the 1st row
print(data[0])

print(len(data))

for k in range(0, len(data)):
    for i in data[k]:
        if k + 1 < len(data):
            for j in data[k + 1]:
                if i < j:
                    break
                else:
                    print(i, j, "are lesser than i")
