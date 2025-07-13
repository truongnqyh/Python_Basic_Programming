# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv
import pandas as pd
# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Specific columns from csv file
selected_columns = df[["species", "sepal_length"]]
print("Selected Columns: \n", selected_columns)

#
filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered Rows: \n", filtered_rows)