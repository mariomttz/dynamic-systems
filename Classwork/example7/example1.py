#!/usr/bin/env python3
#
#
#    vdelaluz@enesmorelia.unam.mx
#    Copyright (C) 2022 Victor De la Luz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import numpy as np
import math
import matplotlib.pyplot as plt

def triangle(x,y,mu,l,s):
    theta = np.arctan(mu)
    n = s*math.sqrt(l*l - math.pow(l/2.0,2))
    Q1 = [(x-(l/2.0)*math.cos(theta)),(y-(l/2.0)*math.sin(theta))]
    Q2 = [(x+(l/2.0)*math.cos(theta)),(y+(l/2.0)*math.sin(theta))]
    Q3 = [(x-n*math.sin(theta)),(y+n*math.cos(theta))]
    return [Q1[0],Q2[0],Q3[0],Q1[0] ] , [Q1[1],Q2[1],Q3[1],Q1[1]]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
#P0
x=0.0
y=0.0
mu=0.0
l=1.0
X, Y = triangle(x,y,mu,l,1)
ax.plot(X,Y)
l1 = l / 3.0
m1 = (Y[2] - Y[0])/(X[2] - X[0])
m2 = (Y[2] - Y[1])/(X[2] - X[1])
m3=mu
#print(m1)
#print(l1)
#print(X[0],Y[0])
#print(X[2],Y[2])
x_r1= (X[0]+X[2])*0.5
y_r1= (Y[0]+Y[2])*0.5
x_r2= (X[2]+X[1])*0.5
y_r2= (Y[2]+Y[1])*0.5
x_r3= x
y_r3= y
ax.scatter(x_r1,y_r1)
ax.scatter(x_r2,y_r2)
ax.scatter(x_r3,y_r3)
X, Y = triangle(x_r1,y_r1,m1,l1,1)
ax.plot(X,Y)
X, Y = triangle(x_r2,y_r2,m2,l1,1)
ax.plot(X,Y)
X, Y = triangle(x_r3,y_r3,m3,l1,-1)
ax.plot(X,Y)
plt.show()
