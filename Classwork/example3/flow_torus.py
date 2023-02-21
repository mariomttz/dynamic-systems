#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Flow function
def F(x, y, t, alpha):
    return (x + t) % 1, (y + alpha * t) % 1

def F_rational(x, y, p, q):
    return (x + q) % 1, (y + p) % 1

t = 0.01
p = 2.0
q = 5.0
alpha = p/q
x0 = 0
y0 = 0
N = 300

itera = np.arange(0, N, 1)
x = x0
y = y0

X = [x0]
Y = [y0]

for i in itera:
    xa, ya = x, y 
    x, y = F(x, y, t, alpha)

    if x > xa and y > ya:
        X.append(x)
        Y.append(y)
    else:
        plt.plot(X, Y)
        X = []
        Y = []

plt.scatter(X, Y)
plt.show()
