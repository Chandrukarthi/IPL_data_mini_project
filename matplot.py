import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [10,20,30,40,50]
y2 = [5,15,25,35,45]

plt.figure(figsize=(8,5), dpi=100)

plt.plot(x, y1, color="red", linestyle="-", linewidth=2, marker="o", markersize=7)
plt.plot(x, y2, color="black", linestyle="--", linewidth=3, marker="*", markersize=15)
plt.annotate( 
    "Highest Value",
    xy=(5,50),
    xytext=(3,50),
    arrowprops=dict(facecolor="grey")
)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Matplotlib")

plt.legend(["Red Line","Green Line",])
plt.grid(True)

plt.savefig("graph.jpg")
plt.show()