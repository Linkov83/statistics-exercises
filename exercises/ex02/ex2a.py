"""Exercise 2A: frequency table and relative-frequency line graph."""
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt

observations = [3.88, 3.90, 3.93, 3.90, 3.93, 3.96, 3.88,
                3.94, 3.96, 3.88, 3.94, 3.99, 3.98]
n = len(observations)
counts = Counter(observations)
prices = sorted(counts)
frequencies = [counts[price] for price in prices]
relative = [frequency / n for frequency in frequencies]
print(f"n = {n}")
print("Price | Frequency | Relative frequency")
for price, frequency, proportion in zip(prices, frequencies, relative):
    print(f"{price:.2f} | {frequency} | {frequency}/{n} = {proportion:.6f}")
print(f"Sum of frequencies = {sum(frequencies)}")
print(f"Sum of relative frequencies = {sum(relative):.12f}")
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(prices, relative, marker="o")
ax.set(xlabel="Gasoline price", ylabel="Relative frequency",
       title="Gasoline Prices in San Francisco")
ax.set_xticks(prices)
ax.grid(alpha=0.3)
fig.tight_layout()
output = Path(__file__).parent / "figures"
output.mkdir(exist_ok=True)
fig.savefig(output / "ex2a_relative_frequency.png", dpi=200)
plt.show()
