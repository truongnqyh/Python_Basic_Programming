import matplotlib.pyplot as plt

# # Line plot
# years = [2010, 2011, 2012, 2013]
# sales = [100, 120, 140, 170]
# plt.plot(years, sales, label="Sales Trend", color="green", marker="o")
# plt.title("Sales over Years")
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

# # Bar Chart
# categories = ["Electionics", "Clothing", "Food", "Pets"]
# revenue = [411, 234, 506, 688]
# plt.bar(categories, revenue, color="red")
# plt.title("Bar Chart")
# plt.show()

# Scatter Plot
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [54, 58, 61, 67, 95]
plt.scatter(hours_studied, exam_scores, color="red")
plt.title("Scatter")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.show()

