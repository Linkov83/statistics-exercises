from pathlib import Path
from statistics import mean, median, stdev
from scipy.stats import shapiro
import matplotlib.pyplot as plt

evaporation = [
    0.02, 0.06, 0.11, 0.14, 0.21, 0.21, 0.21, 0.23,
    0.23, 0.24, 0.25, 0.25, 0.25, 0.26, 0.29, 0.30,
    0.30, 0.32, 0.32, 0.32, 0.33, 0.33, 0.33, 0.33,
    0.34, 0.34, 0.35, 0.35, 0.35, 0.36, 0.36, 0.37,
    0.38, 0.39, 0.40, 0.41, 0.42, 0.42, 0.42, 0.43,
    0.44, 0.44, 0.44, 0.45, 0.45, 0.45, 0.47, 0.48,
    0.48, 0.48, 0.49, 0.49, 0.52, 0.55, 0.56
]

n = len(evaporation)
xbar = mean(evaporation)
s = stdev(evaporation)
lower, upper = xbar - s, xbar + s
k = sum(lower <= x <= upper for x in evaporation)
statistic, p_value = shapiro(evaporation)

print("n =", n)
print(f"Sum = {sum(evaporation):.2f}")
print(f"Mean = {xbar:.5f}")
print(f"Median = {median(evaporation):.2f}")
print(f"Sample standard deviation = {s:.5f}")
print(f"p-value = {p_value:.5f}")
print(f"Interval = [{lower:.6f}, {upper:.6f}]")
print("Count within interval =", k)
print(f"Percentage = {100 * k / n:.2f}%")

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(evaporation, bins=8, edgecolor="black")
ax.set(
    xlabel="Evaporation (cm)",
    ylabel="Frequency",
    title="Evaporation over 55 summer days"
)
fig.tight_layout()

output = Path(__file__).parent / "figures"
output.mkdir(exist_ok=True)
fig.savefig(output / "ex4_histogram.png", dpi=200)
plt.show()