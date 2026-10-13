import numpy as np
import matplotlib.pyplot as plt

# Input data
x = np.array([5, 6, 7, 10, 12, 15, 18, 20], dtype=float)
y = np.array([7.4, 9.3, 10.6, 15.4, 18.1, 22.2, 24.1, 24.8])

# (a) Scatter plot
plt.figure()
plt.scatter(x, y, label="Observations")
plt.xlabel("Moisture content")
plt.ylabel("Finished product density")
plt.title("Moisture Content and Density")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# (b) Assess the relationship
print(
    "A linear model is a reasonable first approximation, "
    "but the relationship flattens at higher moisture levels."
)

# (c) Calculate coefficients using the least-squares formulas
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

B = (
    (np.sum(x * y) - n * x_mean * y_mean)
    / (np.sum(x**2) - n * x_mean**2)
)
A = y_mean - B * x_mean

print(f"\nIntercept A: {A:.6f}")
print(f"Slope B: {B:.6f}")
print(f"Regression model: Y_hat = {A:.6f} + {B:.6f} * x")

# (d) Plot the fitted regression line and observations
y_hat = A + B * x

plt.figure()
plt.scatter(x, y, label="Observations")
plt.plot(x, y_hat, color="red", label="Fitted regression line")
plt.xlabel("Moisture content")
plt.ylabel("Finished product density")
plt.title("Linear Regression: Moisture Content and Density")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# (e) Interpret the slope
print(
    f"\nFor each one-unit increase in moisture content, "
    f"the model predicts an increase of {B:.3f} density units."
)

plt.show()