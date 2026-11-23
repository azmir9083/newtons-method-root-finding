# Newton's Method: Root Approximation (Python)

Uses the **Newton–Raphson method** to find the negative root of

$$e^x = 4 - x^2 \quad\Longleftrightarrow\quad f(x) = e^x + x^2 - 4 = 0$$

correct to **6 decimal places**. The script exports the iteration table and plot data to Excel, so the root can be checked graphically where the curves $y = e^x$ and $y = 4 - x^2$ intersect.

*Course project (Numerical Methods) at San Francisco Bay University.*

## Method

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}, \qquad f'(x) = e^x + 2x$$

The iteration starts at $x_0 = -2$ and stops when $|x_{n+1} - x_n| < 10^{-6}$. It raises an error if the derivative is zero or the method does not converge within 100 iterations.

## Result

**Root ≈ −1.964636**, reached in 3 iterations:

| Iteration | xₙ | f(xₙ) | f′(xₙ) | xₙ₊₁ |
|---:|---:|---:|---:|---:|
| 1 | −2.000000 | 0.135335 | −3.864665 | −1.964981 |
| 2 | −1.964981 | 0.001310 | −3.789804 | −1.964636 |
| 3 | −1.964636 | 0.000000 | −3.789064 | −1.964636 |

## Project Structure

```
newtons-method-root-finding/
├── newtons_method.py   # Newton–Raphson implementation + Excel export
├── plot_data.csv       # x, e^x and 4 − x^2 values for plotting both curves
├── docs/
│   └── report.pdf      # written report with derivation and graphical verification
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.8+
- `numpy`, `pandas`, `openpyxl` (listed in `requirements.txt`)

## How to Run

```bash
git clone https://github.com/azmir9083/newtons-method-root-finding.git
cd newtons-method-root-finding
pip install -r requirements.txt
python newtons_method.py
```

Output:

```
Root of the equation is approximately: -1.9646355974888647
Results saved to: Newtons_Method_Results.xlsx
```

The script creates `Newtons_Method_Results.xlsx` with two sheets: **Iterations** and **Plot Data**. This generated file isn't committed; it's listed in `.gitignore`.

## Author

**Md Azmir Bhuiyan**, Computer Science, San Francisco Bay University · [LinkedIn](https://www.linkedin.com/in/md-azmir-bhuiyan-97174034b)
