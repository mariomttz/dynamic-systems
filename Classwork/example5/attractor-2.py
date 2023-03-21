#!/usr/bin/env python3


#    Smale's Solenoid Attractor (Example 3.9)
#
#    Título	Ergodic Dynamics: From Basic Theory to Applications
#    Volumen    289 de Graduate Texts in Mathematics
#    Autor	Jane Hawkins
#    Editor	Springer Nature, 2021
#    ISBN	3030592421, 9783030592424
#    Largo	336 páginas
#    Copyright (C) 2022 vdelaluz@enesmorelia.unam.mx, mariomttz@comunidad.unam.mx
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
#

import numpy as np
import math
import matplotlib.pyplot as plt 

def F(t,x,y):
    return 2.0*t % 1.0, 0.25*( x + 2.0*math.cos(2.0*math.pi*t)), 0.25*(y+2.0*math.sin(2.0*math.pi*t) )


N_max = 20
delta = 1/N_max

#T = np.arange(0,10000,1) * 0.1
#n = 0.0

N = range(N_max)
r = 0.0

T = []

for n in N:
    r = n * delta
    T.append(r)
    #print(r)


X = range(N_max)
Y = range(N_max)
dx = 1/N_max
dy = 1/N_max

Dx = []
Dy = [] 

for b in Y: 
    y = b*dy
    for a in X:
        x = a*dx
        #y = math.sqrt(1.0 - x*x) 
        #if y <= 1:
        #    print(x,y)
        if math.sqrt(x*x + y*y) <= 1:
            #I
            Dx.append(x)
            Dy.append(y)
            #II
            Dx.append(-x)
            Dy.append(y)
            #III
            Dx.append(-x)
            Dy.append(-y)
            #IV
            Dx.append(x)
            Dy.append(-y)


#T y D
Ft = []
Fx = []
Fy = []
n = 0

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111, projection = '3d')

#for t in T:
#    ax.scatter(t,Dx, Dy)

Ttemp=[]
for t in T:
    Ttemp.append( (2.0*t) % 1.0)

T = Ttemp

n = 0

ax.scatter(Dx, Dy, color='blue')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_title('Attractor (Example 3.9, Hawkings 2021)') 

filename =  '000-attractor.png'
print(filename)
plt.savefig('example2/'+filename )

Tn = len(Dx)

T = np.arange(0, 1 , 1.0/Tn )

for n in range(20):
    Ttemp = []
    Xtemp = []
    Ytemp = []

    plt.cla()
    ax = fig.add_subplot(111, projection = '3d')
    
    for t,x,y in zip(T,Dx,Dy):
        Ttemp.append( (2.0*t) % 1.0)
        Xtemp.append(0.25*( x + 2.0*math.cos(2.0*math.pi*t)))
        Ytemp.append(0.25*(y+2.0*math.sin(2.0*math.pi*t)))

    T = Ttemp
    Dx = Xtemp
    Dy = Ytemp

    ax.scatter(Dx, Dy, color='blue')
    ax.set_title('Attractor (Example 3.9, Hawkings 2021)') 
    ax.set_xlim([-1/(n+1), 1/(n+1)])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1/(n+1), 1/(n+1)])

    filename =  f'{(n+1):03d}' + '-attractor.png'
    print(filename)
    plt.savefig('example2/'+filename )
        
###        
###    for t in T:
###        Ttemp.append( (2.0*t) % 1.0)       
###        Xtemp=[]
###        for x in Dx:
###            Xtemp.append(0.25*( x + 2.0*math.cos(2.0*math.pi*t)))
###        Dx = Xtemp
###        Ytemp=[]
###        for y in Dy:
###            Ytemp.append(0.25*(y+2.0*math.sin(2.0*math.pi*t)))
###        Dy=Ytemp
###        #ax.scatter(t,Dx, Dy)
###        ax.scatter(Dx, Dy,color='blue')
###        ax.set_xlim([-1, 1])
###        ax.set_ylim([-1, 1])
###        #ax.set_zlim([-1, 1])
###    T = Ttemp
###    filename =  f'{n:03d}' + '-attractor.png'
###    print(filename)
###    plt.savefig('example2/'+filename )
###
###
###    #n= n + 1
    
plt.show()


##
##
##for x, y in zip(Dx,Dy):
##    for t in T:
##        a,b,c = F(t,x,y)
##        Ft.append(a)
##        Fx.append(b)
##        Fy.append(c)
##
##
##
##
##Ft = []
##Fx = []
##Fy = []
##n=0
##for p in zip(Ft,Fx,Fy):
##    a,b,c = F(p)
##    Ft.append(a)
##    Fx.append(b)
##    Fy.append(c)
##    
##        
