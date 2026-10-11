# Statistics exercises

Course exercises by Lyubomir Linkov.

## Structure

- `instructions/`: original exercise and submission instructions.
- `warmup/`: optional exercises 1A–1D (not submitted in Moodle).
- `exercises/ex02/`: gasoline prices and frequency tables.
- `exercises/ex03/`: Finnish road traffic accidents and fatalities.
- `exercises/ex04/`: evaporation statistics and normality.
- `exercises/ex05/`: correlation.
- `reports/`: final PDF submissions.

## Setup

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python exercises/ex02/ex2a.py
```

## Solution requirements

For each exercise show the problem representation, formula and intermediate calculations, final answer, and a check that the result makes sense. Use Python for graphs and verification. Submit a PDF in Moodle. Use sample standard deviation with denominator n - 1.

Exercise 2B requires 14 verified 95 E10 prices from August 2026, including dates and stations. Its instruction to sum absolute frequencies to 1 is a typo: relative frequencies sum to 1, absolute frequencies sum to 14. Do not invent observations.

## Progress

- 2A: initial frequency calculation and graph script; final report pending.
- 2B–5B: pending.
