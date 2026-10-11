from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt

# Hintatutka station histories: August 2026, 95 E10, EUR/litre.
observations = [
    ("St1 Helsinki Konala", "2026-08-18", 2.034),
    ("St1 Helsinki Konala", "2026-08-20", 1.939),
    ("St1 Helsinki Konala", "2026-08-30", 1.958),
    ("St1 Helsinki Vartiokylä", "2026-08-02", 1.945),
    ("St1 Helsinki Vartiokylä", "2026-08-31", 1.957),
    ("St1 Helsinki Kivikko", "2026-08-02", 1.952),
    ("St1 Helsinki Kivikko", "2026-08-04", 2.134),
    ("St1 Helsinki Kivikko", "2026-08-05", 1.957),
    ("St1 Helsinki Kivikko", "2026-08-06", 1.958),
    ("St1 Helsinki Kivikko", "2026-08-23", 1.969),
    ("Neste Express Helsinki Mellunmäentie", "2026-08-02", 1.932),
    ("Neste Express Helsinki Mellunmäentie", "2026-08-05", 1.957),
    ("St1 Helsinki Suutarila", "2026-08-23", 1.969),
    ("St1 Helsinki Suutarila", "2026-08-25", 2.109),
]
prices = [price for station, date, price in observations]
n = len(prices)
counts = Counter(prices)
values = sorted(counts)
relative = [counts[value] / n for value in values]
print(f"n = {n}")
print("Price | Frequency | Relative frequency")
for value, proportion in zip(values, relative):
    print(f"{value:.3f} | {counts[value]} | {proportion:.5f}")
print("Sum of frequencies:", sum(counts.values()))
print("Sum of relative frequencies:", sum(relative))

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(values, relative, marker="o")
ax.set(xlabel="95 E10 price (EUR/litre)", ylabel="Relative frequency",
       title="Gasoline prices in Helsinki – August 2026")
ax.set_xticks(values)
ax.set_xticklabels([f"{value:.3f}" for value in values], rotation=45)
ax.set_ylim(bottom=0)
ax.grid(alpha=0.3)
fig.tight_layout()
output = Path(__file__).parent / "figures"
output.mkdir(exist_ok=True)
fig.savefig(output / "ex2b_relative_frequency.png", dpi=200)
plt.show()
