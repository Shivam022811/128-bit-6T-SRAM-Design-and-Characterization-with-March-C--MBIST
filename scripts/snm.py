import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

VDD = 1.8

def largest_square(vin, vout):
    f = lambda x: np.interp(x, vin, vout)
    s_grid = np.linspace(0, VDD, 2001)
    best = 0.0
    for y0 in np.linspace(0, VDD, 1500):
        x0 = f(y0)
        g = f(x0 + s_grid) - (y0 + s_grid)
        ok = np.where(g >= 0)[0]
        if len(ok):
            best = max(best, s_grid[ok[-1]])
    return best

def run(name):
    d = np.loadtxt(f"results/vtc_{name}.txt")
    vin, vout = d[:, 0], d[:, 1]
    snm = largest_square(vin, vout)
    plt.figure()
    plt.plot(vin, vout, label="Curve 1")
    plt.plot(vout, vin, label="Curve 2 (mirror)")
    plt.xlabel("Q (V)")
    plt.ylabel("QB (V)")
    plt.title(f"{name.capitalize()} butterfly, SNM = {snm*1000:.0f} mV")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"results/butterfly_{name}.png", dpi=150)
    print(f"{name.capitalize()} SNM = {snm*1000:.0f} mV")

run("hold")
run("read")