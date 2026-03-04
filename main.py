import numpy as np
np.random.seed(42)
teams = np.array([
    "CSK", "MI", "RCB", "KKR", "SRH",
    "DC", "RR", "PBKS", "GT", "LSG"
])
num_matches = 60

team1 = np.random.choice(teams, num_matches)
team2 = np.random.choice(teams, num_matches)


same = team1 == team2
while np.any(same):
    team2[same] = np.random.choice(teams, np.sum(same))
    same = team1 == team2

score1 = np.random.randint(120, 220, num_matches)
score2 = np.random.randint(120, 220, num_matches)

winner = np.where(score1 > score2, team1, team2)

print("Total Matches:", num_matches)
unique_teams, win_counts = np.unique(winner, return_counts=True)

max_index = np.argmax(win_counts)

print("Most Successful Team:", unique_teams[max_index])
print("Total Wins:", win_counts[max_index])
print("Average Score Team1:", np.mean(score1))

highest_score = np.max(np.maximum(score1, score2))
print("Highest Score:", highest_score)
