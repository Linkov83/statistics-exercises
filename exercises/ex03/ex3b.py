from pathlib import Path
from statistics import mean, median, stdev
import matplotlib.pyplot as plt

years = list(range(2003, 2026))
fatalities = [
    379, 375, 379, 336, 380, 344, 279, 272,
    292, 255, 258, 229, 270, 258, 238, 239,
    211, 223, 225, 196, 185, 181, 193
]

n = len(fatalities)
xbar = mean(fatalities)
squared_deviations = sum((x - xbar) ** 2 for x in fatalities)

print("n =", n)
print("Sum =", sum(fatalities))
print("Sorted values =", sorted(fatalities))
print(f"Mean = {xbar:.2f}")
print("Median =", median(fatalities))
print("Minimum =", min(fatalities))
print("Maximum =", max(fatalities))
print(f"Sum of squared deviations = {squared_deviations:.2f}")
print(f"Sample standard deviation = {stdev(fatalities):.2f}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, fatalities, marker="o")
ax.set(
    xlabel="Year",
    ylabel="Number of fatalities",
    title="Road traffic fatalities in Finland (2025 preliminary)",
    ylim=(0, 420)
)
ax.set_xticks(years[::2])
ax.tick_params(axis="x", rotation=45)
ax.grid(alpha=0.3)
fig.tight_layout()

output = Path(__file__).parent / "figures"
output.mkdir(exist_ok=True)
fig.savefig(output / "ex3b_fatalities.png", dpi=200)
plt.show()