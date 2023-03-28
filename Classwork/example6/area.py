#!/usr/bin/env python3

import numpy as np
# import BigNumber as bn

def f(n): 
    return (2**n + 2**(n-1))

def g(n):
    return (3**(2*n))

i = 0

for x in range(1, 101):
    F = f(x)
    G = g(x)

    i += F/G
    print(x, i)
