import numpy as np
import matplotlib.pyplot as plt

#defining x[n] = (0.5 ^ n) u[n]
n = range(-10, 11)
x = 0.5 * np.ones(len(n))
x = np.power(x, n).tolist()
u = np.heaviside(n, 0.5)
x = np.multiply(x, u).tolist()

#defining x[-n]
x_reverse = x[::-1]

#defining x_e and x_o
x_e = (np.add(x, x_reverse) / 2).tolist()
x_o = (np.subtract(x, x_reverse) / 2).tolist()

#defining frequency domain
N = len(x_o)
n = np.arange(-N/2, N/2)
T = N
w = n/T

DTFT_x_e = np.fft.fft(x_e)
DTFT_x_o = np.fft.fft(x_o)

plt.plot(w, abs(DTFT_x_o / max(abs(DTFT_x_o))), label = "ODD")
plt.plot(w, abs(DTFT_x_e / max(abs(DTFT_x_e))), label = "EVEN")
plt.legend()
plt.show()

DTFT_x_e = np.fft.fftshift(DTFT_x_e)
DTFT_x_o = np.fft.fftshift(DTFT_x_o)

plt.plot(w, abs(DTFT_x_o / max(abs(DTFT_x_o))), label = "ODD")
plt.plot(w, abs(DTFT_x_e / max(abs(DTFT_x_e))), label = "EVEN")
plt.legend()
plt.show()
