import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#defining x(e^(jw)) and y(e^(jw)) coefficeints
y_e_j_w = [1, 2, 0, 1]
x_e_j_w = [1, -0.5, 0.25, 0]

w, h = signal.freqz(y_e_j_w, x_e_j_w)

plt.plot(w, abs(h / max(abs(h))), label = "amplitude")
plt.plot(w, np.imag(h / max(abs(h))), label = "phase")
plt.legend()
plt.show()
