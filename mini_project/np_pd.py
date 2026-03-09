import pandas as pd
import numpy as np

df = pd.read_csv("cleaned_ipl_data.csv")

print(df.head())
print(df.info())

print(df.isnull().sum())

df = df.fillna(0)
df = df.drop_duplicates()

runs_array = np.array(df['total_runs'])

print(np.mean(runs_array))
print(np.max(runs_array))
print(np.min(runs_array))
print(np.std(runs_array))

high_runs = df[df['total_runs'] > 180]
print(high_runs.head())

team_runs = df.groupby('winner')['total_runs'].sum()
print(team_runs)

team_stats = df.groupby('winner')['total_runs'].agg(['sum','mean','max','min'])
print(team_stats)

season_stats = df.groupby('season').agg({
    'total_runs':['sum','mean','max'],
    'wickets':['sum','mean']
})
print(season_stats)

top_matches = df.sort_values(by='total_runs', ascending=False).head(10)
print(top_matches[['match_id','team1','team2','total_runs']])

season_runs = df.groupby('season')['total_runs'].sum()
print(season_runs)

teams1 = df[['match_id','team1']]
teams2 = df[['match_id','team2']]

merged_df = pd.merge(teams1, teams2, on='match_id')
print(merged_df.head())

correlation = df[['total_runs','wickets']].corr()
print(correlation)

most_wins = df['winner'].value_counts()
print(most_wins)

top_players = df['player_of_match'].value_counts().head(10)
print(top_players)

