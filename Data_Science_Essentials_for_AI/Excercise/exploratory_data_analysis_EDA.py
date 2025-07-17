# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
# Inspect Data
df = pd.read_csv(url)
print(df.info())
print(df.describe())

# Handle missing values ~ Age and Embarked
df["Age"] = df["Age"].fillna(df["Age"].median()) ### Median() ~ Ex: 1 - n -> median() = (n/2 + (n/2 +1))/2
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0]) ### mode()[0] ~ "take the first most frequent value"

# Remove duplicates
df = df.drop_duplicates() #  removing duplicate rows from a DataFrame, the rows which are exactly the same as previous ones.

# Filter data: Passengers in the first class
first_class = df[df["Pclass"] == 1]
print("First class passengers: \n", first_class.head())

# Bar chart: Survival rate by class
# survival_by_class = df.groupby("Pclass")["Survived"].mean()
# survival_by_class.plot(kind="bar", color="red")
# plt.title("Survival rate by class")
# plt.xlabel("Pclass")
# plt.ylabel("Surival rate")
# plt.show()

# Histogram: Age distribution
# sns.histplot(df["Age"], kde=True, bins=20, color="green")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# Scatter plt: Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="purple")
plt.title("Relavance between Age and Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
