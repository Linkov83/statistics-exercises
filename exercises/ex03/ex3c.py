from pathlib import Path
import matplotlib.pyplot as plt

years = list(range(2003, 2026))

accidents = [
    6907, 6767, 7022, 6740, 6657, 6881, 6414, 6072,
    6408, 5725, 5334, 5324, 5185, 4752, 4432, 4312,
    4002, 3608, 3243, 3110, 2944, 2811, 2638
]

fatalities = [
    379, 375, 379, 336, 380, 344, 279, 272,
    292, 255, 258, 229, 270, 258, 238, 239,
    211, 223, 225, 196, 185, 181, 193
]

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

axes[0].plot(years, accidents, marker="o")
axes[0].set_ylabel("Number of accidents")
axes[0].set_ylim(0, 8000)

axes[1].plot(years, fatalities, marker="o", color="darkred")
axes[1].set_ylabel("Number of fatalities")
axes[1].set_ylim(0, 420)
axes[1].set_xlabel("Year")
axes[1].set_xticks(years[::2])
axes[1].tick_params(axis="x", rotation=45)

for ax in axes:
    ax.grid(alpha=0.3)

fig.suptitle("Road traffic in Finland (2025 preliminary)")
fig.tight_layout()

output = Path(__file__).parent / "figures"
output.mkdir(exist_ok=True)
fig.savefig(output / "ex3c_comparison.png", dpi=200)
plt.show()