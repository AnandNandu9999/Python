import numpy as np

arr = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

# Printing array dimensions (axis)
print("Array no. of dimensions: ", arr.ndim)

# shape of an array (no. of rows and columns)
print("Shape of array:", arr.shape)

# printing no. of elements in an array
print("No. of elements in array:", arr.size)

# gives the minimum value from 2d array
print("Minimum value in 2d array:", arr.min())

# gives the maximum value from 2d array
print("Maximum value in 2d array:", arr.max())

# prints the diagonal from 2d array
# argument 0 represents the column number
print("Diagonal elements in 2d array:", arr.diagonal(0))

# it views the 2d array
print("View of 2d array:", arr.view())

# prints the data type of 2d array
print("Data type of 2d array elements:", arr.dtype)
