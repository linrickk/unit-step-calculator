# piecewise_builder.py

from dataclasses import dataclass

@dataclass
class StepTerm:
    k: float
    a: float

def build_piecewise(c: float, terms: list[StepTerm]):
    breakpoints = sorted({term.a for term in terms})

    def f_at(t: float) -> float:
        val = c
        for term in terms:
            val += term.k * (1 if t >= term.a else 0)  # u(t-a) with u(0)=1
        return val

    pieces = []

    # Region 1: (-inf, b0)
    if breakpoints:
        b0 = breakpoints[0]
        test = b0 - 1.0
        pieces.append((f"t < {b0}", f_at(test)))
    else:
        # No steps: constant function
        pieces.append(("all t", c))
        return pieces

    # Middle regions: [bi, b(i+1))
    for i in range(len(breakpoints) - 1):
        left = breakpoints[i]
        right = breakpoints[i + 1]
        test = (left + right) / 2.0
        pieces.append((f"{left} ≤ t < {right}", f_at(test)))

    # Last region: t ≥ blast
    blast = breakpoints[-1]
    test = blast + 1.0
    pieces.append((f"t ≥ {blast}", f_at(test)))

    return pieces

def main():
    print("Piecewise Builder for f(t) = c + Σ k*u(t-a)")
    c = float(input("Enter constant c: "))

    n = int(input("How many step terms k*u(t-a)? "))
    terms = []
    for i in range(n):
        k = float(input(f"Term {i+1}: enter coefficient k: "))
        a = float(input(f"Term {i+1}: enter shift a: "))
        terms.append(StepTerm(k=k, a=a))

    pieces = build_piecewise(c, terms)

    print("\nPiecewise form (using u(0)=1 convention):")
    for interval, value in pieces:
        print(f"{interval:>15} : {value:g}")

if __name__ == "__main__":
    main()
