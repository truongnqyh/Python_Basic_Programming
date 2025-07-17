import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv
####### Heatmap
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

del df['species']
# Calculate correlation matrix
correlation_matrix = df.corr()

# plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()