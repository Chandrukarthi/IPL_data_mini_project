import pandas as pd
df = pd.read_csv("cleaned_ipl_data.csv")
print(df.head())
print(df.columns)

group_col = df.columns[0]
num_col = df.select_dtypes(include="number").columns[0]
grouped = df.groupby(group_col)[num_col]

avg_value = grouped.mean()
sum_value = grouped.sum()
count_value = grouped.count()

print("Average:\n", avg_value)
print("Sum:\n", sum_value)
print("Count:\n", count_value)


multi_agg = df.groupby(group_col)[num_col].agg(["mean","sum","count"])
print("Multiple Aggregations:\n", multi_agg)


extra_data = pd.DataFrame({
    group_col: df[group_col],
    "Bonus": [1000]*len(df)
})

merged_df = pd.merge(df, extra_data, on=group_col, how="left")
print("Merged Data:\n", merged_df.head())


if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    print(df[["date","year","month"]].head())


if len(df.select_dtypes(include="number").columns) >= 2:
    corr = df.select_dtypes(include="number").corr()
    print("Correlation Matrix:\n", corr)