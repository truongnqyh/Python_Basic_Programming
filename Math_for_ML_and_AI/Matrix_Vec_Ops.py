import numpy as np

'''
Diagonal Matrix:
 [[0 2 0]
  [0 0 3]]
Identity Matrix:
 [[1. 0. 0. 0.]
  [0. 1. 0. 0.]
  [0. 0. 1. 0.]
  [0. 0. 0. 1.]]
'''
### Matrices ops
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
print("Addition: \n", A + B)            # Add
print("Subtraction: \n", B - A)         # Sub
C = 3 * A
print("Scalar multiplication: \n", C)   # Scalar mul
result = np.dot(A, B)
print("Matrix multiplication: \n", result)  # Matrix mul
I = np.eye(4)
print("Identity Matrix: \n", I)             # Identity Matrix
Z = np.zeros(5)
print("Zero Matrix: \n", Z)                 # Zero Matrix
D = np.diag([1, 2, 3])
print("Diagonal Matrix: \n", D)             # Diagonal Matrix

# Matrix and vector
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
V = np.array([1,0,-1])
result = np.dot(M,V)
print("Matrix-Vector Multiplication: \n", result)

# Identity Matrix multiplicate normal matrix
I = np.eye(3)
M = np.array([[1,2,32],[4,54,6],[7,83,9]])
print("M X I = \n", np.dot(M, I)) ### M X I = M

############################################
'''
Property	           Invertible Matrix	              Singular Matrix
Has inverse?	       ✅ Yes (A⁻¹ exists)	            ❌ No
det(A)	             Not zero (≠ 0)	                  Zero (= 0)
Can solve Ax = b	   Always one unique solution	      May be no or many solutions
Rank	               Full	                            Not full (dependent rows)
'''
A = np.array([[2,3],[1,4]])
determinant = np.linalg.det(A)
print("Determinant of A: ", determinant)