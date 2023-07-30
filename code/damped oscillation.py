import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G


m_pl = (8 * np. pi * G) ** (-1/2)

m = 1  # assumed for simplicity


def damped(t):
    return (m_pl / (np.sqrt(3 * np. pi) * m * t)) * np.sin(m * t)


time = np.linspace(8, 80, 1000)

plt.plot(time, damped(time), color='black')
plt.axhline(y=0, color='grey', linestyle='-', alpha=0.8)
plt.xlabel(r'$t$')
plt.ylabel(r'$\phi$')
plt.savefig('recreated damped.png')
plt.show()




