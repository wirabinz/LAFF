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
m_x, n_x = x.shape
m_y, n_y = y.shape
print(m_x)
print(n_x)
print(m_y)
print(n_y)