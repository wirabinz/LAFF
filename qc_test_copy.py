import numpy as np
import vecvec as laff 


# Define static arrays
x = np.array([[1, 2, 3]])
y = np.array([[0, -1, -2]])
z = np.array([[4, 3, 2, 1]])

def test_ccopy(x, y):
    print("column -> column copy")
    if np.array_equal(laff.copy(x, y), x):
        print("TEST PASSED")
    else:
        print("TEST FAILED")

def test_rcopy(x, y):
    print("\ncolumn -> row copy")
    if np.array_equal(laff.copy(x, np.transpose(y)), np.transpose(y)):
        print("TEST PASSED")
    else:
        print("TEST FAILED")


def test_c2rcopy(x, y):
    print("\nrow -> column copy")
    if np.array_equal(laff.copy(np.transpose(x), y), x):
        print("TEST PASSED")
    else:
        print("TEST FAILED")

def test_r2rcopy(x, y):
    print("\nrow -> row copy")
    if np.array_equal(laff.copy(np.transpose(x), np.transpose(y)), np.transpose(x)):
        print("TEST PASSED")
    else:
        print("TEST FAILED")



# Run the tests with the static arrays

test_ccopy(x, y)

test_rcopy(x,y)

test_c2rcopy(x,y)

test_r2rcopy(x,y)


# Additional test cases    
print("\ncolumn -> column copy (wrong size)")
print(laff.copy(x, z))

print("\ncolumn -> row copy (wrong size)") 
print(laff.copy(x, np.transpose(z)))

print("\nrow -> column copy (wrong size)")
print(laff.copy(np.transpose(x), z))

print("\nrow -> row copy (wrong size)")
print(laff.copy(np.transpose(x), np.transpose(z)))


