import numpy as np

arr = np.array([1,2,3,4]) # [1 2 3 4]
zeroes = np.zeros((3,3)) 
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
ones = np.ones((2,4))
# [[1. 1. 1. 1.]
# [ 1. 1. 1. 1.]]
range_array = np.arange(1, 20, 2) # [ 1  3  5  7  9 11 13 15 17 19]
linspace_array = np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ]

new_arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = new_arr.reshape((2,3))
# [[1 2 3]
#  [4 5 6]]
new_arr1 = np.array({1, 2, 3})
expanded = arr[:, np.newaxis]
#[[1]
# [2]
# [3]
# [4]]
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b) # [5 7 9]
print(a * b) # [ 4 10 18]
print(a / b) # [0.25 0.4  0.5 ]
arr = np.array([4, 9, 36])
print(np.sqrt(arr)) # [2. 3. 6.]
print(np.sum(arr)) # 49
print(np.mean(arr)) # 16.3333333333
print(np.max(arr)) # 36

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2]) # 30
print(arr[-1]) # 60
print(arr[1:4]) # [20 30 40]
print(arr[3:]) #[40 50 60]
reshaped = arr.reshape(2,3)
# [[10 20 30]
#  [40 50 60]]

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original matrix: \n", matrix)
# Tranpose
tranpose = matrix.T
print("Tranpose: \n", tranpose)
