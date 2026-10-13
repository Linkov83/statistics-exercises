import numpy as np
import matplotlib.pyplot as plt

# Input data for 20 subjects
x = np.array([
    165, 167, 180, 155, 212, 175, 190, 210, 200, 149,
    172, 159, 168, 174, 183, 215, 195, 180, 143, 240
], dtype=float)

y = np.array([
    130, 133, 150, 128, 151, 146, 150, 140, 148, 125,
    153, 128, 132, 149, 158, 150, 163, 156, 124, 170
], dtype=float)

# (a, b) Fit the model using the least-squares formulas
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
print(f"Regression model: Y_hat = {A:.6f} + {B:.6f} * x")

# (c) Calculate fitted values, residuals and SSR
y_hat = A + B * x
residuals = y - y_hat
SSR = np.sum(residuals**2)

# (d) Estimate the error standard deviation
sigma_hat = np.sqrt(SSR / (n - 2))

# (e) Standardize residuals using the given formula
standardized_residuals = residuals / sigma_hat

print(f"\nSSR: {SSR:.6f}")
print(f"Estimated error standard deviation: {sigma_hat:.6f}")

print(
    f"\n{'Subject':>8} {'Weight':>8} {'BP':>6} "
    f"{'Fitted':>10} {'Residual':>10} {'Std resid':>10}"
)

for i in range(n):
    print(
        f"{i + 1:8d} {x[i]:8.0f} {y[i]:6.0f} "
        f"{y_hat[i]:10.3f} {residuals[i]:10.3f} "
        f"{standardized_residuals[i]:10.3f}"
    )

# Flag standardized residuals with absolute values above 2
unusual = np.where(np.abs(standardized_residuals) > 2)[0]

print("\nSubjects with |standardized residual| > 2:")
if len(unusual) == 0:
    print("None")
else:
    for i in unusual:
        print(
            f"Subject {i + 1}: "
            f"{standardized_residuals[i]:.3f}"
        )

# (a) Scatter plot and fitted regression line
x_line = np.linspace(x.min(), x.max(), 100)

plt.figure()
plt.scatter(x, y, label="Observations")
plt.plot(
    x_line, A + B * x_line,
    color="red", label="Fitted regression line"
)
plt.xlabel("Weight (lb)")
plt.ylabel("Systolic blood pressure (mmHg)")
plt.title("Weight and Systolic Blood Pressure")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# (f) Standardized residual plot
plt.figure()
plt.scatter(x, standardized_residuals)
plt.axhline(0, color="black", linestyle="--")
plt.axhline(2, color="red", linestyle=":")
plt.axhline(-2, color="red", linestyle=":")

# Label each point with its subject number
for i in range(n):
    plt.annotate(
        str(i + 1),
        (x[i], standardized_residuals[i]),
        xytext=(4, 4),
        textcoords="offset points",
        fontsize=8
    )

plt.xlabel("Weight (lb)")
plt.ylabel("Standardized residual")
plt.title("Standardized Residuals Against Weight")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
