from pathlib import Path
from statistics import mean, median, stdev
import matplotlib.pyplot as plt

# Data from the assignment; 2025 is preliminary.
years = list(range(2003, 2026))
accidents = [
    6907, 6767, 7022, 6740, 6657, 6881, 6414, 6072,
    6408, 5725, 5334, 5324, 5185, 4752, 4432, 4312,
    4002, 3608, 3243, 3110, 2944, 2811, 2638
]

n = len(accidents)
xbar = mean(accidents)
squared_deviations = sum((x - xbar) ** 2 for x in accidents)

print("n =", n)
print("Sum =", sum(accidents))
print("Sorted values =", sorted(accidents))
print(f"Mean = {xbar:.2f}")
print("Median =", median(accidents))
print("Minimum =", min(accidents))
print("Maximum =", max(accidents))
print(f"Sum of squared deviations = {squared_deviations:.2f}")
print(f"Sample standard deviation = {stdev(accidents):.2f}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, accidents, marker="o")
ax.set(
    xlabel="Year",
    ylabel="Number of accidents",
    title="Road traffic accidents in Finland (2025 preliminary)",
    ylim=(0, 8000)
)
ax.set_xticks(years[::2])
ax.tick_params(axis="x", rotation=45)
ax.grid(alpha=0.3)
fig.tight_layout()

output = Path(__file__).parent / "figures"
output.mkdir(exist_ok=True)
fig.savefig(output / "ex3a_accidents.png", dpi=200)
plt.show()