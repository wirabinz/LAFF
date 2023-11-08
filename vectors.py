import numpy as np
import vecvec as laff

x = np.array([[1, 2, 3]])
y = np.array([[0], [0], [0]])
print(y)

x = np.array([[1, 2, 3]])
y = np.array([[0], [0], [0]])
y = laff.copy(x, y)  # Use a different variable 'z' for the copied values
print(y)
