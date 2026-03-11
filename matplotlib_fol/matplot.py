# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y1 = [10,20,30,40,50]
# y2 = [5,15,25,35,45]

# plt.figure(figsize=(8,5), dpi=100)

# plt.plot(x, y1, color="red", linestyle="-", linewidth=2, marker="o", markersize=7)
# plt.plot(x, y2, color="black", linestyle="--", linewidth=3, marker="*", markersize=15)
# plt.annotate( 
#     "Highest Value",
#     xy=(5,50),
#     xytext=(3,50),
#     arrowprops=dict(facecolor="grey")
# )

# plt.xlabel("X Values")
# plt.ylabel("Y Values")
# plt.title("Matplotlib")

# plt.legend(["Red Line","Green Line",])
# plt.grid(True)

# plt.savefig("graph.jpg")
# plt.show()


import matplotlib.pyplot as plt

hours = [1,2,3,4,5]
scores = [55,60,70,80,90]

plt.scatter(hours, scores, color="red")
plt.title("Study Hours vs Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.savefig("study_scatter.png")
plt.show()


players = ["Rohit", "Virat", "Dhoni", "Hardik"]
runs = [80,95,60,70]

plt.bar(players, runs, color="blue")
plt.title("Player Runs")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.savefig("runs_bar.png")
plt.show()

ages = [18,20,22,21,19,23,24,22,20,21]

plt.hist(ages, bins=5, color="green", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_histogram.png")
plt.show()


languages = ["Python","Java","C++","JavaScript"]
students = [40,25,20,15]

plt.pie(students, labels=languages, autopct="%1.1f%%")
plt.title("Programming Language Popularity")
plt.savefig("language_pie.png")
plt.show()