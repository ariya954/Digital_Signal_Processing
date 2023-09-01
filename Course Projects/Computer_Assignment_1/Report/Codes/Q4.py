import numpy as np
import zplane as zp
from scipy import signal
import matplotlib.pyplot as plt

#defining r, w0
r = 0.5
w_0 = np.pi / 2

#defining b and a coefficeints of H(Z)
b = [1, 0 , 0]
a = [1, -2 * r * np.cos(w_0), r ** 2]

zp.zplane(b, a)

#defining x(e^(jw)) and y(e^(jw)) coefficeints of H(Z), Z = e^(jw)
y_e_j_w = [1, 0, 0]
x_e_j_w = [1, -2 * r * np.cos(w_0), r ** 2]

w, h = signal.freqz(y_e_j_w, x_e_j_w)
plt.plot(w, abs(h / max(abs(h))), label = "amplitude")
plt.plot(w, np.imag(h / max(abs(h))), label = "phase")
plt.legend()
plt.show()

w_0 = np.pi / 4
a = [1, -2 * r * np.cos(w_0), r ** 2]
r, p, k = signal.residuez(b, a)
