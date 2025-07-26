# ✅ Link to CSV file (house area vs. price)
csv_path = "https://raw.githubusercontent.com/truongnqyh/Python_Basic_Programming/d346c1b65544b0ba3df40783c5e29e29c4779989/dataset/data_linear.csv"

# ✅ Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Read data from CSV into numpy array
data = pd.read_csv(csv_path).values
N = data.shape[0]  # number of samples

# ✅ Split data into input x (area) and output y (price)
x = data[:, 0].reshape(-1, 1)  # diện tích (m²)
y = data[:, 1].reshape(-1, 1)  # giá nhà

# ✅ Visualize raw data
plt.scatter(x, y)
plt.xlabel('mét vuông')
plt.ylabel('giá')

# ✅ Add bias term (cột toàn 1) để mô hình học được hệ số w[0]
x = np.hstack((np.ones((N, 1)), x))  # x.shape: (N, 2)

# ✅ Initialize weight vector w = [bias, slope]
w = np.array([0., 1.]).reshape(-1, 1)

# ✅ Set training parameters
numOfIteration = 100
cost = np.zeros((numOfIteration, 1))  # store cost at each step
learning_rate = 0.000001

# In gradient descent, we always subtract the gradient from weights:,  w:=w−α⋅∇J(w)
# ✅ Gradient Descent loop
for i in range(1, numOfIteration):
    r = np.dot(x, w) - y  # residuals (errors): predicted - actual
    cost[i] = 0.5 * np.sum(r * r)  # compute squared error loss

    # ✅ Update bias term w[0]
    w[0] -= learning_rate * np.sum(r)

    # ✅ Update slope term w[1]
    w[1] -= learning_rate * np.sum(np.multiply(r, x[:, 1].reshape(-1, 1)))

    # ✅ Print cost to monitor convergence
    print(cost[i])

# ✅ Make predictions using trained model
predict = np.dot(x, w)

# ✅ Plot regression line on top of data points
plt.plot((x[0][1], x[N-1][1]), (predict[0], predict[N-1]), 'r')  # regression line
plt.show()

# ✅ Vẽ biểu đồ cost theo từng vòng lặp
plt.plot(range(1, numOfIteration), cost[1:])
plt.xlabel('Số vòng lặp (iteration)')
plt.ylabel('Cost (MSE)')
plt.title('Cost giảm theo từng vòng lặp')
plt.grid(True)
plt.show()

# ✅ Predict house price for 50m²
x1 = 50
y1 = w[0] + w[1] * 50
print('Giá nhà cho 50m^2 là : ', y1)