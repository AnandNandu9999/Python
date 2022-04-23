import numpy as np

# Creating a 2d array from list with dtype float
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
print("Array created using passed list:", arr)

# creating an array from tuple
tup_ple = np.array((1, 2, 4))
print("Array created using passed tuple:", tup_ple)

# creating an 2d array with zeros of 3 rows and 4 columns
array_with_zeros = np.zeros((3, 4), dtype=int)
print("Array with zeros:", array_with_zeros)

# Create a constant value array of complex type
complex_array = np.full((3, 3), 6, dtype=complex)
print("Array with complex numbers:", complex_array)