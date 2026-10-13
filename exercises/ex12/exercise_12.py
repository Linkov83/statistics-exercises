import numpy as np
import matplotlib.pyplot as plt

# Price and demand data from Exercise 11
x = np.array([50, 40, 35, 30, 20, 15], dtype=float)
y = np.array([88, 112, 123, 136, 158, 172], dtype=float)

# Fit the model using the least-squares formulas
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

B = (
    (np.sum(x * y) - n * x_mean * y_mean)
    / (np.sum(x**2) - n * x_mean**2)
)
A = y_mean - B * x_mean

# (a) Calculate fitted values
y_hat = A + B * x

# (b) Calculate residuals
residuals = y - y_hat

# Print the results for each observation
print(f"Intercept A: {A:.6f}")
print(f"Slope B: {B:.6f}\n")

print(f"{'Price':>8} {'Observed':>12} {'Fitted':>12} {'Residual':>12}")

for price, observed, fitted, residual in zip(x, y, y_hat, residuals):
    print(
        f"{price:8.0f} {observed:12.0f} "
        f"{fitted:12.4f} {residual:12.4f}"
    )

# (c) Calculate the sum of squared residuals
SSR = np.sum(residuals**2)
print(f"\nSum of squared residuals (SSR): {SSR:.6f}")

# (d) Plot residuals against price
plt.scatter(x, residuals, label="Residuals")
plt.axhline(0, color="red", linestyle="--", label="Zero residual")
plt.xlabel("Price")
plt.ylabel("Residual (observed - fitted)")
plt.title("Residual Plot: Price and Demand")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()