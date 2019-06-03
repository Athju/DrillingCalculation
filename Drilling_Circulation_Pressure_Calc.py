Theta600 = float(raw_input("What is the Viscometer reading for theta600?: "))
Theta300 = float(raw_input("What is the Viscometer reading for theta300?: "))

Up = Theta600-Theta300
Yp = Theta300-Up

CollarsID = float(raw_input("What is the inner diameter of the Collars Tubing in inches?: "))
CollarsOD = float(raw_input("What is the outer diameter of the Collars Tubing in inches?: "))
Lc = float(raw_input("What is the Length of the collar in ft?: "))

q = float(raw_input("What is the Mud Pump Rate in ft^3/s: "))
Mud_Density = float(raw_input("What is the density of mud used in lb/gal?: "))

#Function that calculates the Critical Velocity inside the pipe
def Critical_Velocity(ID) :
    Vc = (float(1.08*Up)+float(1.08)*float(((Up**2)+(12.32*8.185*(ID**2))*Yp)**(0.5)))/float(9.185*ID)
    return Vc

Critical_Velocity_Collars = Critical_Velocity(CollarsID)

#Function that calculates the Velocity inside the pipe
def Velocity_inside(d):
    V = q/(float((3.14/4)*((d*0.0833)**2)))
    return V

Velocity_Collars = Velocity_inside(CollarsID)

# If/else statement that compares Critical velocity with actual Velocity inside the collar
if Velocity_Collars > Critical_Velocity_Collars:
    Rec = float((2970*Mud_Density*Velocity_Collars*CollarsID)/(Up))
    print Rec
    fc = raw_input("From the reynolds number and plot what is the Friction facter f?: ")

    Pc = float((fc*Mud_Density*Lc*Velocity_Collars**2)/(25.8*CollarsID))

else:
    Pc = float(Lc*Up*Velocity_Collars/(1500*CollarsID**2))+(float(Lc*Yb/(225*CollarsID)))

PipeID= float(raw_input("What is the inner diameter of the pipe in inches?: "))
PipeOD= flaot(raw_input("What is the outer diameter of the pipe in inches?: "))
Lp= float(raw_input("What is the length of the pipe in ft?: "))

Critical_Velocity_Pipe = Critical_Velocity(PipeID)
Velocity_Pipe = Velocity_inside(PipeID)

if Velocity_Pipe > Critical_Velocity_Pipe:
    Rep = float((2970*Mud_Density*Velocity_Pipe*PipeID)/(Up))
    print Rep
    fp = raw_input("From the reynolds number and plot what is the Friction facter f?: ")

    Pp = float((fp*Mud_Density*Lc*Velocity_Pipe**2)/(25.8*PipeID))

else:
    Pp = float(Lp*Up*Velocity_Pipe/(1500*PipeID**2))+(float(Lp*Yb/(225*PipeID)))

nozzles = float(raw_input("How many nozzles does the drill bit have?: "))
Diameter_Nozzles = float(raw_input("What is the diameter of the nozzles in inches?: "))

Pb = float((Mud_Density*((q*448.831)**2))/(7430*(0.95**2)*(Diameter_Nozzles**4)))

Pressure_Drillstring = float(Pc+Pp+Pb)

print "The Pressure in the drill string is: " , Pressure_Drillstring , " psi"
