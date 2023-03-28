#!/usr/bin/env python3
#
#
#    vdelaluz@enesmorelia.unam.mx
#    pashkov@comunidad.unam.mx
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

MAX = 5

def distance(x1, y1, x2, y2):
    """Returns the Euclidean distance between two points."""

    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def triangle_area(x1, y1, x2, y2, x3, y3):
    """Calculates the area of a triangle with vertices (x1, y1), (x2, y2) and
    (x3, y3).
    """

    # Calculate the distances of each side
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    s = (a + b + c) / 2

    return np.sqrt(s * (s-a) * (s-b) * (s-c))


def insideTriangle(xp, yp, xA, yA, xB, yB, xC, yC):
    """Returns true if the input point (xp, yp) is inside the triangle of
    vertices A(x, y), B(x, y) and C(x, y), or false otherwise.
    """
    #print('computing inside')
    # Calculate area of the entire triangle
    total_area = triangle_area(xA, yA, xB, yB, xC, yC)

    # Calculate the inner areas
    area_1 = triangle_area(xA, yA, xB, yB, xp, yp)
    area_2 = triangle_area(xB, yB, xC, yC, xp, yp)
    area_3 = triangle_area(xA, yA, xC, yC, xp, yp)

    # Verify if point is inside the triangle
    if math.fabs(total_area - (area_1 + area_2 + area_3)) <= 1e-9:
        #print('is inside')
        return True
    else:
        return False


def triangle(x,y,mu,l,xA,yA, xB,yB, xC,yC):
    theta = np.arctan(mu)
    n = math.sqrt(l*l - math.pow(l/2.0,2))
    Q1 = [(x-(l/2.0)*math.cos(theta)),(y-(l/2.0)*math.sin(theta))]
    Q2 = [(x+(l/2.0)*math.cos(theta)),(y+(l/2.0)*math.sin(theta))]
    Q3 = [(x+n*math.sin(theta)),(y-n*math.cos(theta))]
    
    if insideTriangle(Q3[0],Q3[1],xA,yA, xB,yB, xC,yC):
        print(Q3)
        Q3 = [(x-n*math.sin(theta)),(y+n*math.cos(theta))]
        #print('inside!')
        print(Q3)
    return [Q1[0],Q2[0],Q3[0],Q1[0] ] , [Q1[1],Q2[1],Q3[1],Q1[1]]

def computeCoordinates(x, y, l, mu, x_Q1, y_Q1, x_Q2, y_Q2, x_Q3, y_Q3):
    l1 = l / 3.0
    m1 = (y_Q3 - y_Q1)/(x_Q3 - x_Q1)
    m2 = (y_Q3 - y_Q2)/(x_Q3 - x_Q2)
    m3 = mu
    x_r1= (x_Q1+x_Q3)*0.5
    y_r1= (y_Q1+y_Q3)*0.5
    x_r2= (x_Q3+x_Q2)*0.5
    y_r2= (y_Q3+y_Q2)*0.5
    x_r3= x
    y_r3= y
    return l1, m1,m2,m3, x_r1, y_r1, x_r2, y_r2, x_r3, y_r3 

def fractal(n, ax, x, y, mu, l,xA,yA, xB,yB, xC,yC):
    if n > 0:
        X, Y = triangle(x,y,mu,l,xA,yA, xB,yB, xC,yC)
        ax.plot(X,Y,color='b')
        #ax.plot(,Y,color='w')
        l1,m1,m2,m3,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3=computeCoordinates(x,y,l,mu,X[0], Y[0], X[1], Y[1], X[2], Y[2])
        fractal(n-1,ax, x_r1, y_r1,m1,l1,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3)
        fractal(n-1,ax, x_r2, y_r2,m2,l1,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3)
        if n==MAX:
            fractal(n-1,ax, x_r3, y_r3,m3,l1,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')

#P0
x=0.0
y=0.0
mu=0.0
l=1.0
xA = -0.5
yA = 0.0
xB = 0.5
yB = 0
xC=0.0
yC= 0.87

#X, Y = triangle(x,y,mu,l,xA, yA, xB,yB, xC,yC)
#ax.plot(X,Y,color='r')
#l1,m1,m2,m3,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3=computeCoordinates(x,y,l,mu,X[0], Y[0], X[1], Y[1], X[2], Y[2])

X, Y = triangle(x,y,mu,l,xA, yA, xB,yB, xC,yC)

fractal(MAX, ax, x, y, mu, l, X[0], Y[0], X[1], Y[1], X[2], Y[2])


#fractal(MAX-1, ax, x, y, mu, l, X[0], Y[0], X[1], Y[1], X[2], Y[2])
#fractal(MAX-1, ax, x_r2, y_r2,m2,l1,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3)
#fractal(MAX-1, ax, x_r3, y_r3,m3,l1,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3)




#
#
#X, Y = triangle(x,y,mu,l,1)
#ax.plot(X,Y)
#l1,m1,m2,m3,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3=computeCoordinates(x,y,l,mu,X[0], Y[0], X[1], Y[1], X[2], Y[2])
#
#ax.scatter(x_r1,y_r1)
#ax.scatter(x_r2,y_r2)
#ax.scatter(x_r3,y_r3)
#
#X, Y = triangle(x_r1,y_r1,m1,l1,1)
#ax.plot(X,Y)
#
#X, Y = triangle(x_r2,y_r2,m2,l1,1)
#ax.plot(X,Y)
#
#X, Y = triangle(x_r3,y_r3,m3,l1,-1)
#ax.plot(X,Y)

plt.show()
