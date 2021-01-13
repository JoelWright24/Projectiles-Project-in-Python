#See README file for functional discription of this trajectory_computer script
### Moduals and functions to import: ### 
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import minimize

### Main target function ###

def target():
    if __name__ == '__main__':
        while True:
                try:
                    Target_x = float(input("Enter target downrange position in m: "))
                    if (0<Target_x):
                        break
                    else:
                        print("Positive distance please...")
                        ValueError
                except ValueError:
                    print("A valid distnace required. Please Try again...")
        while True:
                try:
                    Target_y=float(input("Enter the height of the target in m: "))
                    if (0<Target_y):
                        break
                    else:
                        print("Positive distance please...")
                        ValueError
                except ValueError:
                    print("A valid distnace required. Please Try again...") 
        while True:
                try:
                    MASS=float(input("Enter the mass of the projectile in kg: "))
                    if (0<MASS):
                        break
                    else:
                        print("Positive mass please...")
                        ValueError
                except ValueError:
                    print("A valid distnace required. Please Try again...")            
        while True:
                try:
                    STARTING_HEIGHT=float(input("Enter the starting hight of the projectile above ground in m: "))
                    if (0<=STARTING_HEIGHT):
                        break
                    else:
                        print("Positive Height please...")
                        ValueError
                except ValueError:
                    print("A valid distnace required. Please Try again...")
        while True:
                try:
                    DRAG_COEFFICIENT=float(input("Enter the drag coefficiant of the projectile: "))
                    if (0<DRAG_COEFFICIENT<1):
                        break
                    else:
                        print("Please give a coefeeiciant in the range of 0 and 1...")
                        ValueError
                except ValueError:
                    print("A valid number between 0 and 1 required. Please Try again...")

        
        def drag_ode (y,t):
            mass = MASS #kg
            Air_densiTarget_y = 1.225 #kgm-3
            Drag_Coefficient = DRAG_COEFFICIENT
            Graviational_Acceleration = 9.81 #ms-2
            Diameter=0.1 #m
            Area= 0.25*math.pi*Diameter**2
            Absolute_VelociTarget_y=math.sqrt((y[0]*y[0])+(y[1]*y[1]))
            constant=-0.5*Air_densiTarget_y*Drag_Coefficient*Area*Absolute_VelociTarget_y/mass
            return([constant*y[0],constant*y[1]-Graviational_Acceleration,y[0],y[1]])   
        
        #solving drag ode with spicy.integrate.odeint
        def solve_ode_spicy (v_0, alpha_deg, STARTING_HEIGHT):
            time_array = np.linspace(0, 100, 1000)           
            Initial_Conditions=[v_0*math.cos(math.pi*alpha_deg/180), v_0*math.sin(math.pi*alpha_deg/180), 0, STARTING_HEIGHT]
            # Now time to return the intergrated drag_ode function with spicy.integrate.odeint.  
            return (odeint(drag_ode, Initial_Conditions, time_array))

        # A function is required to show the difference between the trajectory and target. 
        def objective(x, target):
            objective_Solution = solve_ode_spicy(x[0], x[1], STARTING_HEIGHT)
            length_ans=len(objective_Solution)
            distance_array=np.zeros(length_ans)
            for ii in range (length_ans):
                x_distance=target[0]-objective_Solution[ii,2]
                y_distance=target[1]-objective_Solution[ii,3]
                distance_array[ii]=np.sqrt((x_distance**2)+(y_distance**2))
            #minimum distance from target
            minimum_distance=np.min(distance_array)
            return (minimum_distance)


        counter=0
        tollerence=0.5
        #list of guesses:
        guesses= ((1,45),(5,45),(50,45),(170,45),(240,45),(310,45),(380,45),(450,45),(520,45),(590,45),(660,45),(730,45),(820,45),(1000,45),(1200,45),(1400,45),(1600,45),(1800,45),(2000,45),(2200,45),(2400,45),(2600,45),(2800,45),(3000,45),(3500,45),(4000,45),(4500,45),(5000,45)) 
        #guesses will be x0 for the minimisation. If the solution does not converce then the alogorthim moves on to the next initial guess
        #The boundarys: 
        x0_bound=(0.1,5000)#velociTarget_y bounds
        x1_bound=(10, 80)#angle vounds
        bounds=(x0_bound,x1_bound)
        for i in range (len(guesses)):
            solution= minimize(objective,guesses[i], args=[Target_x,Target_y], bounds=bounds)
            if (solution.fun < tollerence):
                print ("We Hit The Target!")
                print ("Initial Speed       :{:.3f}".format(solution.x[0]))
                print ("Initial Angle       :{:.2f}".format(solution.x[1]))
                print ("Closest distnace    :{:.1e}".format(solution.fun))
                #What is the kinetic energy required?
                Kinietic_Energy=0.5*MASS*(solution.x[0]**2) 
                print ("The kinietic Energy require is: {:.1f}kJ".format(Kinietic_Energy/1000))
                # gunpowder has 3000 joules per gram
                Gunpowder_mass=Kinietic_Energy/3000000
                print ("Which is the equivilent to the use of around {:.3f}kg of gunpowder.".format(Gunpowder_mass))
               
                YesOrNo = input("Do you require an image of the flight? [y/n]: ")
                if (YesOrNo=="y"):
                    #plotting a graph 
                    v_0=solution.x[0]
                    alpha_deg=solution.x[1]
                    chart=solve_ode_spicy(v_0, alpha_deg, STARTING_HEIGHT)
                    plt.figure(1)
                    plt.scatter(Target_x, Target_y, marker=(5, 1) , label="Target")
                    plt.plot(chart[:,2],chart[:,3],color='orange',label='Trajectory')
                    plt.ylim([0,1.1*np.max(chart[:,3])])
                    plt.xlabel('distance in x')
                    plt.ylabel('distance in y')   
                    plt.grid(None, 'both', 'both')
                    plt.legend()
                    plt.show()
                    break
                else:
                    break
            else: 
                counter=counter+1
            if (counter==len(guesses)):
                print ("Target was missed")                
        return (solution) 

job=target()