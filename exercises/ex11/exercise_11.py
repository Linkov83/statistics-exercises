import numpy as np
import matplotlib.pyplot as plt

# Input data
x = np.array([50, 40, 35, 30, 20, 15], dtype=float)
y = np.array([88, 112, 123, 136, 158, 172], dtype=float)

# (b) Calculate coefficients using the least-squares formulas
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

B = (
    (np.sum(x * y) - n * x_mean * y_mean)
    / (np.sum(x**2) - n * x_mean**2)
)
A = y_mean - B * x_mean

print(f"Intercept A: {A:.6f}")
print(f"Slope B: {B:.6f}")
print(f"Regression model: Y_hat = {A:.6f} + ({B:.6f}) * x")

# (c) Predict demand at a price of 25
price = 25
predicted_demand = A + B * price

print(f"\nPredicted demand at price 25: {predicted_demand:.3f} units")
print(f"Approximately {predicted_demand:.0f} units.")

# (d) Interpret the slope
print(
    f"\nFor each one-unit increase in price, "
    f"the model predicts a decrease of {abs(B):.3f} units ordered."
)

# (a) Scatter plot, with the fitted line added
x_line = np.linspace(x.min(), x.max(), 100)
y_line = A + B * x_line

plt.scatter(x, y, label="Observations")
plt.plot(x_line, y_line, color="red", label="Fitted regression line")
plt.scatter(
    price,
    predicted_demand,
    color="green",
    marker="x",
    s=100,
    label="Prediction at price 25"
)

plt.xlabel("Price")
plt.ylabel("Number of units ordered")
plt.title("Price and Demand")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()