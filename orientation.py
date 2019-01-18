# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:07:12 2019

@author: longiag
"""

#print("Hello World!")
import numpy as np

#m = 1.0
#v = 5.0
#T1 = 0.5*m*v**2 #KE (can be written in many different ways, T1-T4) 
#T2 = 1/2 *m * v * v
#T3 = 0.5 * m * v* v
#T4 = m*v**2/2 

#print(T1, T2, T3, T4)

#PE: need 2 particles, need 2 charges and distance betweent them 
#particle 1 
#m1 = 1.0   #mass
#v1 = 5.0   #velocity 
#q1 = 1.0   #charge 
#x1 = 0.0 #position 

#particle 2
#m2 = 1.0
#v2 = 2.5
#q2 = 1.0
#x2 = 0.5

# variables for pair of particles 
#r12 = np.sqrt((x1-x2)**2) #distance between the 2 particles 
#V12= q1*q2/r12            #PE 
#print("separation is ", r12)
#print("Potential Energy is ", V12)

Npart= 10
#creating empty lists 
m= np.zeros(Npart) 
v= np.zeros(Npart)
q= np.zeros(Npart)
x= np.zeros(Npart)
T = np.zeros(Npart)

#print(m)

#using the for-loop to assign #s
for i in range(0,Npart):
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5 * i
    v[i] = 0.2 *i 
    T[i] = 0.5 * m[i] * v[i]**2
#print(m)
#print(q)
#print(x)
#print(v)
    
 # now that we have mass and velocity for the ith particle
 #I can calculate the KE for the ith particle 
 
     
     
print (T)


