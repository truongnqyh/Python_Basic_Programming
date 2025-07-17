import pandas as pd

df = pd.DataFrame({
    "Class": ["A", "B", "A", "B", "C", "C"],
    "Score": [85, 90, 88, 72, 95, 80],
    "Age": [15, 16, 15, 17, 16, 15],
})

print("Original Dataset \n", df)
grouped = df.groupby("Class").mean()
print(grouped)