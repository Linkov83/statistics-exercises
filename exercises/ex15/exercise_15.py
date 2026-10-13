import numpy as np

# Input data from Exercise 14
x = np.arange(1, 11, dtype=float)
y = np.array([
    0.50, 0.90, 1.20, 1.35, 1.50,
    1.60, 1.53, 1.38, 1.21, 0.65
])

np.set_printoptions(precision=6, suppress=True)

# (a) Construct the design matrix and response vector
X = np.column_stack((np.ones(len(x)), x, x**2))
Y = y.reshape(-1, 1)

print("Design matrix X:")
print(X)

print("\nResponse vector Y:")
print(Y)

# (b) Calculate X transpose times X and X transpose times Y
XTX = X.T @ X
XTy = X.T @ Y

print("\nXTX:")
print(XTX)

print("\nXTy:")
print(XTy)

# (c) Construct the same matrix using the sums
n = len(x)
sum_x = np.sum(x)
sum_x2 = np.sum(x**2)
sum_x3 = np.sum(x**3)
sum_x4 = np.sum(x**4)

matrix_from_sums = np.array([
    [n,      sum_x,  sum_x2],
    [sum_x,  sum_x2, sum_x3],
    [sum_x2, sum_x3, sum_x4]
], dtype=float)

print("\nMatrix constructed from sums:")
print(matrix_from_sums)

print(
    "XTX matches the matrix from sums:",
    np.allclose(XTX, matrix_from_sums)
)

# (d) Construct the same right-hand side using the sums
vector_from_sums = np.array([
    [np.sum(y)],
    [np.sum(x * y)],
    [np.sum(x**2 * y)]
])

print("\nVector constructed from sums:")
print(vector_from_sums)

print(
    "XTy matches the vector from sums:",
    np.allclose(XTy, vector_from_sums)
)

# (e) Solve the matrix normal equations
beta = np.linalg.solve(XTX, XTy)
B0, B1, B2 = beta.ravel()

print(f"\nB0: {B0:.6f}")
print(f"B1: {B1:.6f}")
print(f"B2: {B2:.6f}")

# Compare with the sum-based normal equations from Exercise 14
beta_from_sums = np.linalg.solve(
    matrix_from_sums, vector_from_sums
)

print(
    "Coefficients match the sum-based solution:",
    np.allclose(beta, beta_from_sums)
)

# (f) Explain the connection
print(
    "\nThe matrix equation represents the same normal equations "
    "as in Exercise 14. XTX contains the sums of powers of x, "
    "and XTy contains the sums involving y. "
    "Both methods therefore give the same coefficients."
)