import numpy as np

# is_vector(x) check whether an array is a vector or not 
def is_vector(arr):
    """Check if arr is a vector."""
    
    if arr.ndim == 1:
        return True
    
    # Higher dimension case
    elif arr.ndim > 1:
      
        # Shape (1, n) is a vector 
        if arr.shape[0] == 1:
            return True
        
        # Otherwise check if all dims except first are size 1
        else: 
            return all(size == 1 for size in arr.shape[1:])
        
    else:
        return False

# y = copy (x,y) copies vector x into vector y
# Vector x and y can be a mixture of column and/or row vector. 
# In other words, x and y can be n x 1 or 1 x n arrays. 
# However, one size must equal to 1 and the other size equal n 

# The reason y is an imput paramter is that the input y indicates whether 
# the output, y_out, is a column or row vector. 

# And then also indicates whether x must be transposed (e.g. if x is arow vector and y is a column vector).

def copy(x, y):
    m_x, n_x = x.shape
    m_y, n_y = y.shape

    if not (is_vector(x) and is_vector(y)):
        return 'Failed. x and y should be a vector'

    if not (m_x * n_x == m_y * n_y):
        return 'Failed. x dimension is not proportionate to y dimension'

    if n_x == 1:  # x is a column
        if n_y == 1:  # y is a column
            for i in range(m_x):
                y[i, 0] = x[i, 0]
        else:  # y is a row
            for i in range(m_x):
                y[0, i] = x[i, 0]
    else:  # x is a row
        if n_y == 1:  # y is a column
            for i in range(n_x):
                y[i, 0] = x[0, i]
        else:  # y is a row
            for i in range(n_x):
                y[0, i] = x[0, i]

    return y