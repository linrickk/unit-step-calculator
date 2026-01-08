# step_graph.py
# step_graph.py  (mathplotlib)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

def unit_step(x: np.ndarray, at_zero: float = 1.0) -> np.ndarray:
    y = np.zeros_like(x, dtype=float)
    y[x > 0] = 1.0
    y[x < 0] = 0.0
    y[x == 0] = at_zero
    return y


def main():
    print("Matplotlib Unit Step Graph: f(t) = c + A*u(t-a)")

    # Inputs
    A = float(input("Enter amplitude A (default 1): ") or "1")
    a = float(input("Enter shift a (default 0): ") or "0")
    c = float(input("Enter constant c (default 0): ") or "0")

    at_zero_raw = input("Value at the step point (t=a). Choose 1 or 0 (default 1): ").strip()
    at_zero = float(at_zero_raw) if at_zero_raw else 1.0

    # Range
    t_min = float(input("Enter t_min (default -5): ") or "-5")
    t_max = float(input("Enter t_max (default 5): ") or "5")
    n_points = int(input("Number of points (default 1000): ") or "1000")

    if t_max <= t_min:
        print("t_max must be greater than t_min. Using defaults -5 to 5.")
        t_min, t_max = -5.0, 5.0

    # Build signal
    t = np.linspace(t_min, t_max, n_points)
    u = unit_step(t - a, at_zero=at_zero)
    f = c + A * u

    # Plot
    plt.figure()
    plt.plot(t, f)
    plt.axvline(a, linestyle="--")  # shows where the step happens
    plt.title("f(t) = c + A·u(t-a)")
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
