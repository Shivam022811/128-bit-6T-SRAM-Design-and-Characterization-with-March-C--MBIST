import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = np.loadtxt("results/inverter.txt")
vin, vout = data[:, 0], data[:, 1]

plt.plot(vin, vout, label="Vout")
plt.plot(vin, vin, "--", label="Vout = Vin")
plt.xlabel("Vin (V)")
plt.ylabel("Vout (V)")
plt.title("CMOS inverter VTC (SKY130, TT)")
plt.grid(True)
plt.legend()
plt.savefig("results/inverter_vtc.png", dpi=150)
print("Saved results/inverter_vtc.png")
