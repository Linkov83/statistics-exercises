import numpy as np
import matplotlib.pyplot as plt

# Input data
x = np.arange(1, 11, dtype=float)
y = np.array([
    0.50, 0.90, 1.20, 1.35, 1.50,
    1.60, 1.53, 1.38, 1.21, 0.65
])

# (a) Scatter plot
plt.figure()
plt.scatter(x, y)
plt.xlabel("Coded amount of drug")
plt.ylabel("Tumor weight reduction (g)")
plt.title("Drug Amount and Tumor Reduction")
plt.grid(True, alpha=0.3)
plt.tight_layout()

print(
    "A straight-line model does not appear appropriate. "
    "Tumor reduction first increases and then decreases."
)

# (b) Calculate sums for the normal equations
n = len(x)
sum_x = np.sum(x)
sum_x2 = np.sum(x**2)
sum_x3 = np.sum(x**3)
sum_x4 = np.sum(x**4)

sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2y = np.sum(x**2 * y)

# Coefficient matrix of the normal equations
normal_matrix = np.array([
    [n,      sum_x,  sum_x2],
    [sum_x,  sum_x2, sum_x3],
    [sum_x2, sum_x3, sum_x4]
], dtype=float)

# Right-hand side of the normal equations
normal_rhs = np.array([
    sum_y,
    sum_xy,
    sum_x2y
])

# Solve the equations without a ready-made regression function
B0, B1, B2 = np.linalg.solve(normal_matrix, normal_rhs)

print("\nNormal equation matrix:")
print(normal_matrix)

print("\nRight-hand side:")
print(normal_rhs)

print(f"\nB0: {B0:.6f}")
print(f"B1: {B1:.6f}")
print(f"B2: {B2:.6f}")
print(
    f"Quadratic model: Y_hat = {B0:.6f} "
    f"+ {B1:.6f} * x + ({B2:.6f}) * x**2"
)

# (d, e) Find the maximum of the fitted quadratic curve
if B2 < 0:
    x_max = -B1 / (2 * B2)
    y_max = B0 + B1 * x_max + B2 * x_max**2

    print(f"\nCoded drug amount at maximum: {x_max:.6f}")
    print(f"Maximum predicted tumor reduction: {y_max:.6f} g")
    print(f"Maximum is within the observed range: {x.min() <= x_max <= x.max()}")
else:
    raise ValueError("The fitted quadratic has no downward-opening maximum.")

# (c) Plot the fitted curve with the observations
x_curve = np.linspace(x.min(), x.max(), 300)
y_curve = B0 + B1 * x_curve + B2 * x_curve**2

plt.figure()
plt.scatter(x, y, label="Observations")
plt.plot(
    x_curve, y_curve,
    color="red", label="Fitted quadratic curve"
)
plt.scatter(
    x_max, y_max,
    color="green", marker="x", s=100,
    label="Predicted maximum"
)
plt.xlabel("Coded amount of drug")
plt.ylabel("Tumor weight reduction (g)")
plt.title("Quadratic Regression: Drug Effectiveness")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.show()