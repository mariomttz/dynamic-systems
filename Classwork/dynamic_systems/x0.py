#!/usr/bin/env python3

'''
Author: Mario Martinez.
Contact: mariomttz@protonmail.com

Created on: February 07, 2023.
Under MIT license.

'''

# Libraries

import matplotlib.pyplot as plt
import numpy as np

# Code

def f(x, a, b):
    return a * x + b

# New array

X0 = np.arange(1, 50, 1)

for x0 in X0:
    a = -0.5
    b = 2.0
    N = 10

    print("a = " + str(a))
    print("b = " + str(b))
    print("x0 = " + str(x0))
    print("N = " + str(N))

    i = np.arange(0, N, 1)
    x = x0
    X = []

    for _ in i:
        print(x)
        X.append(x)
        x = f(x, a, b)

    plt.plot(X)

#plt.ylim([0, 100])
#plt.yscale("log")
plt.show()
