import numpy as np
import vecvec as laff

# x = np.array([[1, 2, 3]])
# y = np.array([[0], [0], [0]])
#print(y)



x = np.array([[1, 2, 3]])
y = np.array([[0], [0], [0]])
check1 = laff.copy(x,y)  # Use a different variable 'z' for the copied values
#print(y)


x = np.array([[1, 2, 3]]) 
y = np.array([[0, -1, -2]])
z = np.array([[4, 3, 2, 1]])

# Example usage:
alpha = 2  # Scalar alpha (not an array)
x = np.array([[1, 2, 3]])  # Row vector x

# Using direct multiplication creates a new array
result_direct = alpha * x

# Using laff.scal modifies the array in-place
result_laff = laff.scal(alpha, x)

check = np.array_equal(result_direct, result_laff)
print(check)