from pathlib import Path
from statistics import mean, stdev
import matplotlib.pyplot as plt

hours = [6, 14, 3, 22, 9, 11, 12, 5, 18, 24, 15, 17]
gpa = [2.8, 3.2, 3.1, 3.6, 3.0, 3.3, 3.4, 2.7, 3.1, 3.8, 3.0, 3.9]

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(hours, gpa)
ax.set(
    xlabel="Weekly study time (hours)",
    ylabel="GPA",
    title="Study hours and GPA"
)
ax.grid(alpha=0.3)
fig.tight_layout()

output = Path(__file__).parent / "figures"
output.mkdir(exist_ok=True)
fig.savefig(output / "ex5a_scatter.png", dpi=200)
plt.show()

n = len(hours)
xbar, ybar = mean(hours), mean(gpa)
sx, sy = stdev(hours), stdev(gpa)
numerator = sum(
    (x - xbar) * (y - ybar)
    for x, y in zip(hours, gpa)
)
r = numerator / ((n - 1) * sx * sy)

print(f"Mean hours = {xbar:.5f}")
print(f"Mean GPA = {ybar:.5f}")
print(f"sx = {sx:.5f}, sy = {sy:.5f}")
print(f"Numerator = {numerator:.2f}")
print(f"Correlation r = {r:.5f}")