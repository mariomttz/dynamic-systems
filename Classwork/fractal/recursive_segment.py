#!/usr/bin/env python3

def divide(N, a, b, n):
    if n < N:
        c = (a+b)/2

        divide(N, a, c, n+1)
        print(f'Lim. Inf {a}, Pun. Medio {c}, Lim. Sup {b}')
        divide(N, c, b, n+1)
        print(f'Lim. Inf {a}, Pun. Medio {c}, Lim. Sup {b}')

divide(3, 0, 1, 0)
