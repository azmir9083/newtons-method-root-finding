"""
Newton's Method: approximate the negative root of e^x = 4 - x^2
(i.e. f(x) = e^x + x^2 - 4 = 0), correct to 6 decimal places.

Writes the iteration table and plot data to an Excel file so the
root can be verified graphically (intersection of e^x and 4 - x^2).
"""
import numpy as np
import pandas as pd

# Define the function f(x) and its derivative f'(x)
def f(x):
    return np.exp(x) + x**2 - 4

def f_prime(x):
    return np.exp(x) + 2 * x

# Newton's Method Implementation
def newtons_method(x0, tolerance=1e-6, max_iterations=100):
    iterations = []
    for i in range(max_iterations):
        fx = f(x0)
        fpx = f_prime(x0)
        if fpx == 0:  # Avoid division by zero
            raise ValueError("Derivative is zero. No convergence.")
        x1 = x0 - fx / fpx
        iterations.append((i + 1, x0, fx, fpx, x1))
        if abs(x1 - x0) < tolerance:
            return x1, iterations
        x0 = x1
    raise ValueError("Maximum iterations reached without convergence.")

# Initial guess
initial_guess = -2

# Perform Newton's Method
root, iteration_data = newtons_method(initial_guess)

# Generate data for Excel plotting
x_values = np.linspace(-3, 1, 500)
y_exp = np.exp(x_values)
y_poly = 4 - x_values**2

# Prepare dataframes for Excel
iteration_df = pd.DataFrame(iteration_data, columns=["Iteration", "x_n", "f(x_n)", "f'(x_n)", "x_(n+1)"])
plot_df = pd.DataFrame({
    "x": x_values,
    "y_exp": y_exp,
    "y_poly": y_poly
})

# Save results to an Excel file
excel_path = "Newtons_Method_Results.xlsx"  # saved next to where the script is run
with pd.ExcelWriter(excel_path) as writer:
    iteration_df.to_excel(writer, sheet_name="Iterations", index=False)
    plot_df.to_excel(writer, sheet_name="Plot Data", index=False)

print(f"Root of the equation is approximately: {root}")
print(f"Results saved to: {excel_path}")
