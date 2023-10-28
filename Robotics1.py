import numpy as np

T1=0  # theta in degrees
T2=0

a1 = 1
a2 = 1  # every length in cm
a3 = 1
a4 = 1

T1=(T1/180.0)*np.pi
T2=(T2/180.0)*np.pi    #theta in radians

R0_1 = [[np.cos(T1),-np.sin(T1),0],[np.sin(T1),np.cos(T1),0],[0,0,1]]
R1_2 = [[np.cos(T2),-np.sin(T2),0],[np.sin(T2),np.cos(T2),0],[0,0,1]]

R0_2 = np.dot(R0_1,R1_2)

#print(R0_2)

d0_1 = [[a2*np.cos(T1)],[a2*np.sin(T1)],[a1]]
d1_2 = [[a4*np.cos(T2)],[a4*np.sin(T2)],[a3]]

print(np.matrix(d0_1))
print(np.matrix(d1_2))