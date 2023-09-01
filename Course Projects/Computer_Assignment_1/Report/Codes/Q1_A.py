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

x_e = (np.add(x, x_reverse) / 2).tolist()
x_o = (np.subtract(x, x_reverse) / 2).tolist()

plt.plot(n, x_o, label = "ODD")
plt.plot(n, x_e, label = "EVEN")
plt.legend()
plt.show()
