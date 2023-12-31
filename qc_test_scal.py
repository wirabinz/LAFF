import numpy as np
import vecvec as laff

alpha = np.array(-2)  # Scalar alpha (not an array)
x = np.array([[1, 2, 3]])  # Row vector x


# test with x row vector 
def test_rscal(alpha, x):
    print("\nrow vector x")
    result_direct=alpha*x
    result_laff=laff.scal(alpha,x)
    if np.array_equal(result_laff, result_direct):
        print("TEST PASSED")
    else:
        print("TEST FAILED")

# test with x column vector 
def test_cscal(alpha, x):
    print("\ncolumn vector x")
    result_direct=alpha*np.transpose(x)
    result_laff=laff.scal(alpha,np.transpose(x))
    if np.array_equal(result_laff, result_direct):
        print("TEST PASSED")
    else:
        print("TEST FAILED")

# test with illegal alpha
def test_illscal(alpha, x):
    alpha=alpha*x
    result_direct=alpha*x
    result_laff=laff.scal(alpha,x)
    print("\nr vector x")
    if not np.array_equal(result_laff, result_direct):
        print("TEST PASSED")
    else:
        print("TEST FAILED")

# Running test
# print(alpha*x)
# print(laff.scal(alpha,x))

test_rscal(alpha, x)
test_cscal(alpha, x)
test_illscal(alpha, x)

