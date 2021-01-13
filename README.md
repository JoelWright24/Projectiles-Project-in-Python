# Projectiles Project
## Overview
This project shows how to encomporate a drag function to calculate the flight of a spherical projectile, with diameter 0.1m, ignoring the effects of wind.
## User given information  
After the target function is called, the user is required to provide the following five pices of information: 
- The location of a target in x and y coordinates; 
- The mass of the projectile; 
- The starting height above ground; 
- And finally the drag coefficiant of the projectile.

The is code around each of these inputs so that only the right information may be entered. 

The information output is:
- The initial speed required to hit the target; 
- The initial angle required to hit the target;
- The energy required to do this and the equivilent amount of gunpowder; 
- An optional graphical plot of the trajectory of the projectile.

## Nested Functions
After The target function is made of other nested functions, as follows: 
1. Drag_ode
2. Solve_ode_spicy
3. Objective

### Drag_ode
Fistly, the function Drag_ode takes inital velocity and displacement, in the form y=[vx, vy, rx, ry] and uses the user input informaiton and output the acceleration and velociy of the next time step. 

### Solve_ode_scipy
Solve_ode_spicy plots the trajectory of projectile, over a given time span. The user inputs the Drag_ode function, the inital contions for the projectile, calculated from the inital velocity, inital angle and the inital height. The scipy.intergrate.odeint then intergrates this over the time funtion to provide an array providing velocity and positon of the cartesian co-ordinates throughout the given time period.
 
### Objective
Objective function is used to caluclate the difference bewteen the position along a trajectory of the projectile, and a given target. The function inputs are the location of the target, in the form [(x,y)] and the function calls solve_ode_spicy, then writes an array of equal lenth with the minimum distance to the target. The minimum distance from this array is returned.

## Optimising the Objective Function
The rest of the target function optimises the objective function. This is done through use of scipy.optimize.minimize. 

In order for the minimize function to operate, it requires an initial guess of the velocity and angle inputs. The initial guesses are in a long list and they span between the bounds. The cartesian coordinates of the target are places in the arguments. Bounds are also given for the maximum and minimum inital velocity and the maximum and minimum inital angle.   

The minimize function may solve to a local minimum. Therefore it is import to give required minimum tolerence that the solution must be within, so that the target function has hit the target. 

Multiple initial conditions through out the domain of the bounds are given, and these are cycled through a for loop. The loop is broken if the solution to the optimisation is less than the tollerence. 

## Solution Information Provided
When a good solution is found, information is printed - the initial speed, the inital angle and the closeset distance to the coordinates given for the target. The kinetic energy required to fire the projectile is given and the equivilent amount of gun powder. The user is then given the option to return a graph of the projectile. This is only returnes if the user returns "y".