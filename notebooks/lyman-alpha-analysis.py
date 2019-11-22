import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

filename = '../data/lyman-alpha.txt'
k, pk, err = np.loadtxt(filename, unpack=True)

fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_ylabel('Pk')
ax.set_xscale('log')
ax.set_xlabel('k')
ax.errorbar(k, pk, yerr=err, fmt='.')

plt.show()
