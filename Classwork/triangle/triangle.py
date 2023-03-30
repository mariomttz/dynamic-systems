#!/usr/bin/env python3

# Equilateral triangle
# Mario Alberto Martinez Oliveros
# TIC's - UNAM ENES Morelia
# mariomttz@comunidad.unam.mx

import matplotlib.pyplot as plt
import numpy as np

def equilateral_triangle(side_size: int) -> plt.plot:
    x = np.array([0, side_size, side_size/2, 0])
    y = np.array([0, 0, side_size, 0])

    plt.plot(x, y, '-')
    plt.show()

equilateral_triangle(int(input("Triangle side size: ")))
