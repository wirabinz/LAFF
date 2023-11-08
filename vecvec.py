import numpy as np

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

    if not (np.ndim(x) == 1 and np.ndim(y) == 1):
        print('copy failed')
        return 'FAILED'

    if not (m_x * n_x == m_y * n_y):
        print('copy failed')
        return 'FAILED'

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