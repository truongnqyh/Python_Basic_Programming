import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

####### Heatmap
data = np.random.rand(5,5)
print(data)
# sns.heatmap(data, annot=True, cmap="coolwarm")
# plt.title("Heatmap")
# plt.show()

######## Scatter plot
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.scatter(x, y, color = "green")
# plt.title("Scatter plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend(["Dataset 1"])
# plt.show()

######## Histogram
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(data, bins=4, color="red", edgecolor="black")
# plt.title("Histogram")
# plt.show()

######## Bar Chart
# categories = ["A", "B", "C"]
# values = [10, 15, 7]
# plt.bar(categories, values, color="blue")
# plt.title("Bar Chart")
# plt.show()
######## Basic Plot
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.plot(x,y)
# plt.show()

######### Line plot
# plt.plot([1, 2, 3], [10, 20, 30], label="Trend", color="purple", linestyle="-.", marker="x")
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# # Show the label
# plt.legend()
# plt.show()