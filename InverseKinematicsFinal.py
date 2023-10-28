#Defining Libraries
import math
import time
import numpy

#Defining Link Lengths
d1 = 15
d2 = 45
d3 = 50
d4 = 21
d5 = 6

#Defining Rotation Matrix
nx = 1
ny = 0
nz = 0

sx = 0
sy = -1
sz = 0

ax = 0
ay = 0
az = -1

#Defining Position Matrix OR Take user input
x = 20
y = 78 #Keep small box along the blue line
z = 38


#Defining Angle Constraints Function
def angleconstraint(angle):
    if 0 > angle > -90:
        angle = angle + 90
    if 0 > angle < -90:
        angle = abs(angle) + 90
    if 90 < angle < 180:
        angle = angle - 90
    if 90 < angle > 180:
        angle = angle - 180  # or 270 - angle1
    return angle

#Defining Demap Function for 2nd Motor
def linear_convert(value, input_min, input_max, output_min, output_max):
  demapangle = (value - input_min) / (input_max - input_min) * (output_max - output_min) + output_min
  return demapangle

#Main Loop
while True:

    #All Inverse Kinematics Equations ( Sshhhhhhhh It is a Secret !!!)
    q1 = math.atan2(y, x)

    eq1 = -(ax * math.cos(q1) + ay * math.sin(q1))
    eq2 = (-az)

    q5 = math.atan2((nx * math.sin(q1) - ny * math.cos(q1)), (sx * math.sin(q1) - sy * math.cos(q1)))

    c = (x / math.cos(q1)) + (d5 * eq1) - (d4 * eq2)
    d = (d1 - (d4 * eq1) - (d5 * eq2) - z)

    R = (c * c + d * d - d3 * d3 - d2 * d2) / (2 * (d3 * d2))
    t = math.sqrt(1 - R * R)

    q3 = math.atan2(t, R)

    r = d3 * math.cos(q3) + d2
    s = d3 * math.sin(q3)

    q2 = math.atan2((r * d) - (s * c), (r * c) + (s * d))

    eq3 = math.atan2(-(ax * math.cos(q1) + ay * math.sin(q1)), -az)
    q4 = eq3 - (q2 + q3)

    #Converting angles in radians to degrees
    angle1 = q1 * (180 / math.pi)
    angle2 = q2 * (180 / math.pi)
    angle3 = q3 * (180 / math.pi)
    angle4 = q4 * (180 / math.pi)
    angle5 = q5 * (180 / math.pi)

    #Calling the AngleContraints
    angle1 = angleconstraint(angle1)
    angle2 = angleconstraint(angle2) 
    angle3 = angleconstraint(angle3)
    angle4 = angleconstraint(angle4)
    angle5 = angleconstraint(angle5)

    #Calling DeMap
    angle2 = linear_convert(angle2, 0, 360, 0, 8192)

    #Printing the angles
    # print("Theta1 =", math.ceil(angle1))
    # print("Theta2 =", math.ceil(angle2))
    # print("Theta3 =", math.ceil(angle3))      #You can remove this OKKKKK
    # print("Theta4 =", math.ceil(angle4))
    # print("Theta5 =", math.ceil(angle5))

    #F*ck the loop we got what we want
    break

#Defining Poses

theta10 = 90
theta20 = 0
theta30 = 80
theta40 = 0
theta50 = 90

# print("Pose1 Theta1 =", math.ceil(theta10))
# print("Pose1 Theta2 =", math.ceil(theta20))
# print("Pose1 Theta3 =", math.ceil(theta30))       #You can remove this OKKKKK
# print("Pose1 Theta4 =", math.ceil(theta40))
# print("Pose1 Theta5 =", math.ceil(theta50))

theta11 = 90
theta21 = 0
theta31 = 80
theta41 = 0
theta51 = 90

# print("Pose2 Theta1 =", math.ceil(theta11))
# print("Pose2 Theta2 =", math.ceil(theta21))
# print("Pose2 Theta3 =", math.ceil(theta31))       #You can remove this OKKKKK
# print("Pose2 Theta4 =", math.ceil(theta41))
# print("Pose2 Theta5 =", math.ceil(theta51))

#Now giving orderwise 

for i in range(0,3):
    if i == 0 :
        print("Theta1 =", math.ceil(angle1))
        print("Theta2 as Counts =", numpy.abs(math.ceil(angle2) + 135 + 36))
        print("Theta3 =",math.ceil(angle3) + 16)
        print("Theta4 =", 90 - math.ceil(angle4) + 5)
        print("Theta5 =", math.ceil(angle5) + 5)
        print("\n")
        time.sleep(5)

    if i == 1 :
        print("Pose1 Theta1 =", math.ceil(theta10))
        print("Pose1 Theta2 =", math.ceil(theta20))
        print("Pose1 Theta3 =", math.ceil(theta30))      
        print("Pose1 Theta4 =", math.ceil(theta40))
        print("Pose1 Theta5 =", math.ceil(theta50))
        print("\n")
        time.sleep(5)

    if i == 2 :
        print("Pose2 Theta1 =", math.ceil(theta11))
        print("Pose2 Theta2 =", math.ceil(theta21))
        print("Pose2 Theta3 =", math.ceil(theta31))
        print("Pose2 Theta4 =", math.ceil(theta41))
        print("Pose2 Theta5 =", math.ceil(theta51))
        print("\n")
        time.sleep(5)

#Formation of 4x4 matrix for Homogenous Transformation

x1 = 0
y1 = 88
z1 = 120
matrix1 = numpy.matrix([[1,0,0,x1],[0,-1,0,y1],[0,0,-1,z1],[0,0,0,1]])
print(matrix1)