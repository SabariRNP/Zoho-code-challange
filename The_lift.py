# The lift
# A 12 story building has 6 lifts at a center. Lifts are scattered along multiple ﬂoors. Assume a
# user calls lift from N th ﬂoor. Write a program to ﬁnd the nearest lift for pickup and track all
# the lift movements and current location
# Assume lifts are in this ﬂoors -> 3,G,6,12,10,11
# For example
# Input
# Lift positions
# 3,G,6,12,10,11
# Enter your floor number: 7
# Nearest lift number: 3 //Explanation: Lift
# floor
# Enter your floor number: 8
# Nearest lift: 3 //Explanation: Lift
# floor in above transition
# number 3 is currently in 6th
# number 3 is moved from 6th floor to 7th



lift_pos=['3','G','6','12','10','11']
print("Current Lift positions: ", lift_pos)
 
while 1:
    floor = str(input("Enter your floor: "))
    if(floor == "G"):
        floor = 0
        
    floor = int(floor)
    
    nearestLift = 0, 
    diff = 13
    for i, Lpos in enumerate(lift_pos):
        cLPos = Lpos
        if(cLPos == "G"):
            cLPos = 0
        cLPos = int(cLPos)
        
        if(abs(cLPos - floor)  < diff):
            nearestLift = i+1
            diff = abs(cLPos - floor)
        
    if(diff == 0):
        print("Lift {} is already at the requested floor".format(nearestLift))
    else:
        print("Nearest list is : ", nearestLift)
        
    if(floor == 0):
        floor = "G"
        
    lift_pos[nearestLift-1] = floor
    print("Current Lift positions: ", lift_pos)
    
    stop  = str(input("Are You want to call the lift again(Y/N):\t"))
    if(stop != "Y" and stop != "y"):
        break
