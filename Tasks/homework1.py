#!/usr/bin/env python3

'''
Author: Mario Martinez.
Contact: mariomttz@protonmail.com

Created on: February 11, 2023.
Under MIT license.

'''

# Libraries

import matplotlib.pyplot as plt
import numpy as np

# Code
def f(x, r):
    return x + r - x**2

# Initial conditions
X0 = np.arange(0.1, 0.2, 0.1)
R = [0.1, 0.5, 1.0, 1.1, 1.5, 1.6]

for i, r in enumerate(R):
    print(f"r = {r}")

    for x0 in X0:
        I = np.arange(0, 30, 1)
        x = x0
        X = []

        for _ in I:
            X.append(x)
            x = f(x, r)

        plt.subplot(2, 3, i+1)
        plt.title(f"r = {r}")
        plt.ylim(0, 2)
        plt.plot(X)

plt.show()
