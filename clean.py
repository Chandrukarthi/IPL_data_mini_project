import pandas as pd
import numpy as np
ds = pd.read_csv("ipl data.csv")
print("First 5 rows:\n", ds.head())
print("\nColumns:\n", ds.columns)
print("\nDataset Info:\n")
print(ds.info())
print("\nMissing values count:\n", ds.isnull().sum())
numeric_cols = ds.select_dtypes(include=np.number).columns
for col in numeric_cols:
    ds[col] = ds[col].fillna(ds[col].mean())
ds = ds.fillna("Unknown")
print("\nAfter filling missing values:\n", ds.head())

ds = ds.drop_duplicates()

print("\nAfter removing duplicates:\n", ds.head())

for col in numeric_cols:
    ds[col] = ds[col].astype(int)

ds.to_csv("cleaned_ipl_data.csv", index=False)
