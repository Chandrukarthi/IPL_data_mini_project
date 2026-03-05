import pandas as pd

# Load the CSV file
df = pd.read_csv("ipl data.csv")

# Show first 5 rows
print(df.head())

# Show last 5 rows
print(df.tail())

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Top 50 rows
top50 = df.head(50)
print(top50)

# Matches with total_runs > 200
high_score = df[df['total_runs'] > 200]
print(high_score)

# Sort by total runs
sorted_runs = df.sort_values(by='total_runs', ascending=False)
print(sorted_runs.head(20))

# Count matches won by each team
wins = df['winner'].value_counts()
print(wins)

# Top 10 Player of the Match awards
pom = df['player_of_match'].value_counts().head(10)
print(pom)

# Group by season and find average runs
season_avg = df.groupby('season')['total_runs'].mean()
print(season_avg)