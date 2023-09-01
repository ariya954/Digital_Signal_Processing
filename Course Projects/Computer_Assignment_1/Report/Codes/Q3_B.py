import numpy as np
import matplotlib.pyplot as plt

delta = np.zeros(100)
delta[0] = 1
h = np.zeros(100)

#defining h[n]
h[0] = delta[0]
h[1] = 2 * delta[0] + 0.5 * h[0]
h[2] = 0.5 * h[1] - 0.25 * h[0]
for i in range(3, 100):
    h[i] = (delta[i])+ (2 * delta[i - 1]) + (delta[i - 3]) + (0.5 * h[i - 1]) - (0.25 * h[i - 2])

#defining frequency domain
N = len(h)
n = np.arange(-N/2, N/2)
T = N
w = n/T

#defining h(e^(jw))
h_e_j_w = np.fft.fftshift(np.fft.fft(h))

plt.plot(w, abs(h_e_j_w / max(abs(h_e_j_w))), label = "amplitude")
plt.plot(w, np.imag(h_e_j_w / max(abs(h_e_j_w))), label = "phase")
plt.legend()
plt.show()
