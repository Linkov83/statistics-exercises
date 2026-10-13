# Statistics Exercises

Research Methods coursework at Metropolia University of Applied Sciences.

Author: Lyubomir Linkov.

Python scripts implement statistical calculations and create graphs. Written solutions are prepared separately for submission in Moodle.

## Contents

| Folder | Contents |
| --- | --- |
| `instructions/` | Exercise documents and submission instructions |
| `exercises/ex02/` | Gasoline price frequency tables and relative frequency graphs |
| `exercises/ex03/` | Finnish road traffic statistics and comparison graphs |
| `exercises/ex04/` | Evaporation statistics, histogram, Shapiro-Wilk test and standard deviation interval |
| `exercises/ex05/` | Study hours/GPA correlation and a perfect negative correlation example |
| `exercises/ex09/` | Descriptive statistics and a line graph of Finnish traffic fatalities |
| `exercises/ex10/` | Linear regression of moisture content and density |
| `exercises/ex11/` | Price and demand regression with prediction |
| `exercises/ex12/` | Fitted values, residuals and sum of squared residuals |
| `exercises/ex13/` | Weight and blood pressure regression with standardized residuals |
| `exercises/ex14/` | Quadratic regression of drug effectiveness |
| `exercises/ex15/` | Design matrix and matrix form of the normal equations |

Exercises 6-8 have written probability and reliability solutions and no Python scripts in this repository. Exercise 3D is a written check of calculations and graphs.

## Setup

The scripts were run on Windows using Python 3.14.

From the repository root, create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Or Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

Run each command separately from the repository root.

### Descriptive statistics and correlation

```bash
python exercises/ex02/ex2a.py
python exercises/ex02/ex2b.py
python exercises/ex03/ex3a.py
python exercises/ex03/ex3b.py
python exercises/ex03/ex3c.py
python exercises/ex04/ex4.py
python exercises/ex05/ex5a.py
python exercises/ex05/ex5b.py
python exercises/ex09/ex9.py
```

### Regression

```bash
python exercises/ex10/exercise_10.py
python exercises/ex11/exercise_11.py
python exercises/ex12/exercise_12.py
python exercises/ex13/exercise_13.py
python exercises/ex14/exercise_14.py
python exercises/ex15/exercise_15.py
```

Close all graph windows to let each script finish. Exercise 5A prints its numerical results after the graph window closes.

Earlier plotting scripts save PNG files in their exercise's `figures/` folder. Exercises 10-14 display their graphs but do not automatically save them. Exercise 15 prints matrix calculations and does not create a graph.

## Regression methods

Exercises 10-13 calculate the intercept and slope directly using the least-squares formulas.

Exercise 14 constructs the quadratic normal equations from the required sums and solves them using `np.linalg.solve()`.

Exercise 15 constructs the design matrix with columns `1`, `x` and `x**2`, calculates `X.T @ X` and `X.T @ Y`, and solves the same normal equations in matrix form.

No ready-made regression functions such as `np.polyfit` or `sklearn.linear_model.LinearRegression` are used.

For Exercise 13, standardized residuals follow the assignment formula: each residual is divided by `sqrt(SSR / (n - 2))`.

## Data sources

- Exercise 2A: gasoline prices supplied in the exercise document.
- Exercise 2B: 14 observations of 95 E10 prices from five Helsinki stations in August 2026, from [Hintatutka](https://www.hintatutka.net/explore/suomi/uusimaa/helsinki?range=custom&from=2026-08-01&to=2026-08-31&group=day&fuels%5B%5D=95e10).
- Exercises 3 and 9: [Statistics Finland, StatFin Table 12sc](https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/StatFin__ton/12sc.px/), values reproduced from the exercise document for 2003-2025. The 2025 data are preliminary.
- Exercises 4 and 5: supplied evaporation and study hours/GPA data. Exercise 5B uses `y = 12 - 2x`.
- Exercises 10-15: moisture/density, price/demand, weight/blood pressure and drug effectiveness data supplied in the regression exercise document.

## Conventions

- Sample standard deviation uses `n - 1`.
- Absolute frequencies sum to the number of observations.
- Relative frequencies sum to 1, apart from rounding.
- The Shapiro-Wilk test uses significance level 0.05. Not rejecting normality does not prove a normal distribution.
- Correlation does not establish causation.
- Residuals are observed values minus fitted values.
- Regression calculations use full precision; displayed results are rounded.

Written submissions include the formulas, reasoning, results, graphs and checks required by the course instructions.