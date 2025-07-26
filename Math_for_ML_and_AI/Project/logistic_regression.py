# ✅ Link to CSV file (house area vs. price)
csv_path = "https://raw.githubusercontent.com/truongnqyh/Python_Basic_Programming/dedf024319dcd5e931ce3f256f052012f45e42a8/dataset/data_logistic.csv"

### output is binary value (0,1) then need SIGMOID function
"""
Thiết lập model:
    Hàm sigmoid: sigma(x) = 1 / (1 + exp(-x))
    y_hat_i = sigmoid(w0 + w1 * x1_i + w2 * x2_i) 
            = sigmoid(np.dot(x, w))
            = 1 / (1 + exp(-(w0 + w1*x1 + w2*x2)))
Thiết lập loss function
    L = - (y_i * log(y_hat_i) + (1 - y_i) * log(1 - y_hat_i))
Tìm tham số bằng việc tối ưu loss function
Dự đoán dữ liệu mới bằng model vừa tìm được
"""

# ✅ Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ✅ Read data from CSV into numpy array
data = pd.read_csv(csv_path).values
N, d = data.shape
x = data[:, 0:d-1].reshape(-1, d-1)
y = data[:, 2].reshape(-1, 1)

x_accept = x[y[:, 0] == 1]  # các mẫu được cho vay
x_reject = x[y[:, 0] == 0]  # các mẫu bị từ chối

# ✅ Visualize raw data
# Vẽ biểu đồ
plt.scatter(x_accept[:, 0], x_accept[:, 1], c='red', edgecolors='none', s=30, label='cho vay')
plt.scatter(x_reject[:, 0], x_reject[:, 1], c='blue', edgecolors='none', s=30, label='từ chối')
plt.legend(loc=1)
plt.xlabel('mức lương (triệu)')
plt.ylabel('kinh nghiệm (năm)')
plt.title('Phân loại khách hàng theo thu nhập và kinh nghiệm')
plt.grid(True)
plt.show()
