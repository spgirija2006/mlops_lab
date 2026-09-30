
import numpy as np
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, np.nan, 30, 22, 35],
    "Salary": [50000, 60000, np.nan, 45000, 80000],
    
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)

print("\n--- Data Info & Missing Value Counts ---")
print(df.info()) 
print(df.isnull().sum())


df["Age"] = df["Age"].fillna(df["Age"].median())
print("\n--- After Handling Missing Values ---")
print(df)

