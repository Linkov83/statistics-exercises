from pathlib import Path
from statistics import mean, stdev
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [12 - 2 * value for value in x]

xbar, ybar = mean(x), mean(y)
sx, sy = stdev(x), stdev(y)
numerator = sum(
    (xi - xbar) * (yi - ybar)
    for xi, yi in zip(x, y)
)
r = numerator / ((len(x) - 1) * sx * sy)

print("Pairs:", list(zip(x, y)))
print("Means:", xbar, ybar)
print("Sum of cross deviations:", numerator)
print(f"sx = {sx:.5f}, sy = {sy:.5f}")
print(f"r = {r:.5f}")

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(x, y)
ax.set(xlabel="x", ylabel="y", title="y = 12 - 2x")
ax.set_xticks(x)
ax.grid(alpha=0.3)
fig.tight_layout()

output = Path(__file__).parent / "figures"
output.mkdir(exist_ok=True)
fig.savefig(output / "ex5b_scatter.png", dpi=200)
plt.show()