import math
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#Initial condition, t=0 (j=0)
for i in range(Nx+1):
    u(i,0) = f(i*dx)

#Boundary condition, x=0 (i=0) and x=L (i=Nx)
for j in range(1,Nt+1):
    u(0,j) = g1(j*dt)
    u(Nx,j) = g2(j*dt)

#Final formula (inside mesh)
for j in range(Nt):
    for i in range(1,Nx):
        u(i,j+1) = r*u(i-1,j) + (1-2*r)*u(i,j) + r*u(i+1,j)

