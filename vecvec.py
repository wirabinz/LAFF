import numpy as np

# is_scalar(x) check whether a variable is a scalar or not 
def is_scalar(arr):

    if  isinstance(arr, (int, float,np.integer, np.floating)):
        return True
    elif arr.ndim==0:
        return True

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

# y = copy(x,y) copies vector x into vector y
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

# x_out = laff_scal( alpha, x ) scales vector x by alpha
# Vector x a column or row vector.  In other words, x can be 
# a n x 1 or 1 x n array.  However, one size must equal 1 and the 
# other size equal n. 

# For convenience, we treat x as a m x n matrix where either m or n
# equals 1, making it a row or column vector.
# Extract the row and column sizes of alpha and x

def scal(alpha, x):
    m_x, n_x = x.shape

    if not (is_vector(x)):
        return 'Failed. x  should be a vector.'
    
    if not(is_scalar(alpha)):
        return 'Failed. Alpha is not a scalar.'
    
    if n_x == 1:  # x is a column vector
    # Scale the elements of x
        for i in range(m_x):
            x[i, 0] = alpha * x[i, 0]

    elif m_x == 1:  # x is a row vector
        # Scale the elements of x
        for i in range(n_x):
            x[0, i] = alpha * x[0, i]

    else:  # x is neither a row nor a column vector
        return 'Failed. x is not a vector'

    return x

# y_out = laff_axpy( alpha, x, y ) computes y_out = alpha * x + y.
#   Vectors x and y can be a mixture of column and/or row vector.  In other
#   words, x and y can be n x 1 or 1 x n arrays.  However, one size must 
#   equal 1 and the other size equal n.  
# 
#   The reason y is an input parameter is that the input y indicates 
#   whether the output, y_out, is a column or row vector.
# For convenience, we treat each vector as a m x n matrix where either m 
# or n equals 1, making it a row or column vector.
# Extract the row and column sizes of alpha, x, and y

#  For convenience, we treat each vector as a m x n matrix where either m 
#  or n equals 1, making it a row or column vector.

def axpy(alpha, x,y):
    # Check if alpha is a scalar
    if not(is_scalar(alpha)):
        return 'Failed. Alpha is not a scalar.'