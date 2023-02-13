#! /usr/bin/python3    

#Diogo de Macedo

import numpy as np
import matplotlib.pyplot as plt

# Set up initial conditions

g = 9.8 #acceleration due to gravity, in m/s^2
m = 1 #mass of the projectile, in Kg
v_0 = 80 #initial velocity, in m/s
phi = 45 #launch angle, in degrees
alpha = 0.005 #drag coefficient, adimensional 
dt = 0.1 #timestep, seconds


# Set up lists to store values

t = [0] #keeps track of time

x = [0] #updates positions in the x-direction
y = [0] #updates positions in the y-direction 

v_x = [v_0*np.cos(phi/180*np.pi)] #intial velocity in x-direction
v_y = [v_0*np.sin(phi/180*np.pi)] #initial position in y-direction
v_total = [v_0]

# Drag Force
F_d= alpha*(v_0**2)

# Now that the drag force has been determined, acceleration can be calculated using Newton's 2nd Law

a_x = [-(F_d*np.cos(phi/180*np.pi))/m]        
a_y = [-g-(F_d*np.sin(phi/180*np.pi)/m)]


# Update lists through a numerical approximation method
counter = 0
while (y[counter] >= 0):                   # Check that the last value of y is >= 0
    t.append(t[counter]+dt)                # increment by dt and update time list
    
    #update velocity
    
    v_x.append(v_x[counter]+dt*a_x[counter])
    v_y.append(v_y[counter]+dt*a_y[counter])
    v_total.append(np.sqrt(v_x[-1]**2 + v_y[-1]**2))        #magnitude of the velocity vector
    
    
    # Update position
    
    x.append(x[counter]+dt*v_x[counter])    
    y.append(y[counter]+dt*v_y[counter])
    
    # With the updated velocity calculate the drag force and then update acceleration
    vel = np.sqrt(v_x[counter+1]**2 + v_y[counter+1]**2)   # magnitude of the velocity
    F_d = alpha*vel**2                                     # drag force 
    a_x.append(-(F_d*np.cos(phi/180*np.pi))/m)     
    a_y.append(-g-(F_d*np.sin(phi/180*np.pi)/m))
    
    # increment the counter
    counter = counter +1
    
# Make plots

plt.figure(1)
plt.subplot(211)
plt.title("Ballistic Curve")
plt.plot(x,y,'ro')
plt.ylabel("y (m)")
plt.subplot(212)
plt.plot(x,v_total, 'b')
plt.ylabel("Velocity,v(m/sec) ")
plt.xlabel("Position, x(m)")
plt.show()
