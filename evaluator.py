# unit_step_evaluator.py

def unit_step(x: float, at_zero: int = 1) -> int:
    """
    Heaviside unit step u(x).
    at_zero controls the value at x = 0 (commonly 1, sometimes 0, sometimes 0.5).
    """
    if x > 0:
        return 1
    if x < 0:
        return 0
    return at_zero

def shifted_step(t: float, a: float, at_zero: int = 1) -> int:
    """Compute u(t - a)."""
    return unit_step(t - a, at_zero=at_zero)

def main():
    print("Unit Step Evaluator: computes u(t-a)")
    print("Type a single t, or a list like: -2,-1,0,1,2")
    at_zero = input("Value at the step point (t=a). Choose 1 or 0 (default 1): ").strip()
    at_zero = int(at_zero) if at_zero else 1

    a = float(input("Enter shift a: "))

    t_raw = input("Enter t (single number or comma-separated list): ").strip()
    if "," in t_raw:
        t_list = [float(s) for s in t_raw.split(",")]
        results = [(t, shifted_step(t, a, at_zero=at_zero)) for t in t_list]
        print("\nResults:")
        for t, y in results:
            print(f"t={t:>8g}  u(t-a)={y}")
    else:
        t = float(t_raw)
        y = shifted_step(t, a, at_zero=at_zero)
        print(f"\nFor t={t}, a={a}: u(t-a) = {y}")

if __name__ == "__main__":
    main()
