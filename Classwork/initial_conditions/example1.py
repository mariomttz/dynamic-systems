#!/usr/bin/env python3

'''
Author: Mario Martinez.
Contact: mariomttz@protonmail.com

Created on: February 09, 2023.
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

for x0 in X0:
    r = 0.5
    N = 20

    print("r =" + str(r))
    print("N =" + str(N))

    i = np.arange(0, N, 1)
    x = x0
    X = []

    for _ in i:
        print(x)
        X.append(x)
        x = f(x, r)
    plt.plot(X)

plt.show()
