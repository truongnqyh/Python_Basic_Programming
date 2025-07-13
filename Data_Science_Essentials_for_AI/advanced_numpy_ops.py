import numpy as np

# Array and sca;ar broadcasting
arr = np.array([1, 2, 3])
print(arr + 10) # [11 12 13]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
print(matrix + vector) 
# [[2 2 4]
#  [5 5 7]]

arr = np.array([[1,2,3], [4,5,6]])
print("Sum: ", np.sum(arr)) # 21
print("Mean: ", np.mean(arr)) # 3.5
print("Max: ", np.max(arr)) # 6
print("Min: ", np.min(arr)) # 1
"""
Standard Deviation formula:  (square root of the average of squared differences from the mean)

    σ = sqrt( (1/n) * Σ(xᵢ - x̄)² )

Where:
    - n is the number of elements
    - xᵢ is each individual value
    - x̄ is the mean (average)
"""
print("Standard Deviation: ", np.std(arr)) # 1.707825127659933
print("Sum along rows: ", np.sum(arr, axis=1))  # [ 6 15]
print("Sum along columns: ", np.sum(arr, axis=0)) # [5 7 9]

arr = np.array([[1,2,3,4,5,6]])
evens = arr[arr % 2 == 0]  # [2 4 6]
arr[arr > 3] = 0 # [[1 2 3 0 0 0]]

# Create random array or matrix

# To keep the same matrix or array each run time
np.random.seed(42)

random_array = np.random.rand(3,3)
print(random_array)
'''
 [[0.53895746 0.67623855 0.43383039]
 [0.61485583 0.46704402 0.40768535]
 [0.36353125 0.35987952 0.25644515]]
'''
random_int_matrix = np.random.randint(0, 10, size=(2,3))
print(random_int_matrix)
'''
 [[1 5 3]
 [9 8 5]]
'''
