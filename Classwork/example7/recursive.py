#!/usr/bin/env python3

# Recursive

def suma(n):
    if n == 2:
        print(str(n), end='')
        return 2

    print(str(n) + '+', end='')
    return suma(n-2) + (1 / (n)) ** 2

print('=' + str(suma(10)))

#suma = 0
#for i in range(10):
#    suma = suma + 1
#
#print(suma)
