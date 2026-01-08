from flask import Flask, request, render_template, send_file, jsonify
import io
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

app = Flask(__name__)


def unit_step(x, at_zero=1.0):
    y = np.zeros_like(x, dtype=float)
    y[x > 0] = 1.0
    y[x < 0] = 0.0
    y[x == 0] = at_zero
    return y


@app.get("/")
def home():
    return render_template("index.html")


# ✅ 1) Evaluator
@app.get("/api/eval")
def api_eval():
    t = float(request.args.get("t", "0"))
    a = float(request.args.get("a", "0"))
    at_zero = float(request.args.get("at_zero", "1"))

    x = t - a
    result = float(unit_step(np.array([x]), at_zero=at_zero)[0])

    return jsonify({"t": t, "a": a, "x": x, "result": result})


# ✅ 2) Piecewise
@app.post("/api/piecewise")
def api_piecewise():
    data = request.get_json(force=True)

    c = float(data.get("c", 0))
    at_zero = float(data.get("at_zero", 1))
    terms = data.get("terms", [])

    if not terms:
        return jsonify({"pieces": [{"interval": "all t", "value": c}]})

    breakpoints = sorted(set(float(term["a"]) for term in terms))

    def f_at(tval):
        val = c
        for term in terms:
            k = float(term["k"])
            a = float(term["a"])
            val += k * float(unit_step(np.array([tval - a]), at_zero=at_zero)[0])
        return float(val)

    pieces = []
    pieces.append({"interval": f"t < {breakpoints[0]}", "value": f_at(breakpoints[0] - 1)})

    for i in range(len(breakpoints) - 1):
        left = breakpoints[i]
        right = breakpoints[i + 1]
        mid = (left + right) / 2
        pieces.append({"interval": f"{left} ≤ t < {right}", "value": f_at(mid)})

    pieces.append({"interval": f"t ≥ {breakpoints[-1]}", "value": f_at(breakpoints[-1] + 1)})

    return jsonify({"pieces": pieces})


# ✅ 3) Graph
@app.get("/plot.png")
def plot_png():
    A = float(request.args.get("A", "1"))
    a = float(request.args.get("a", "0"))
    c = float(request.args.get("c", "0"))
    at_zero = float(request.args.get("at_zero", "1"))

    t = np.linspace(-5, 5, 1000)
    f = c + A * unit_step(t - a, at_zero=at_zero)

    fig = plt.figure()
    plt.plot(t, f)
    plt.axvline(a, linestyle="--")
    plt.title("f(t) = c + A·u(t-a)")
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.grid(True)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

