import numpy as np

T1=0
T2=0
T3=0
T4=0
T5=0
T6=0

T1=(T1/180.0)*np.pi
T2=(T2/180.0)*np.pi
T3=(T3/180.0)*np.pi
T4=(T4/180.0)*np.pi
T5=(T5/180.0)*np.pi
T6=(T6/180.0)*np.pi

R0_1 = [[np.cos(T1),0,np.sin(T1)],[np.sin(T1),0,-np.cos(T1)],[0,1,0]]
R1_2 = [[-np.sin(T2),0,np.cos(T2)],[np.cos(T2),0,np.sin(T2)],[0,1,0]]
R2_3 = [[1,0,0],[0,1,0],[0,0,1]]
R3_4 = [[np.cos(T4),0,-np.sin(T4)],[np.sin(T4),0,np.cos(T4)],[0,-1,0]]
R4_5 = [[np.cos(T5),0,np.sin(T5)],[np.sin(T5),0,-np.cos(T5)],[0,1,0]]
R5_6 = [[np.cos(T6),-np.sin(T6),0],[np.sin(T6),np.cos(T6),0],[0,0,1]]

R0_2 = np.dot(R0_1,R1_2)
R2_4 = np.dot(R2_3,R3_4)
R4_6 = np.dot(R4_5,R5_6)
R0_4 = np.dot(R0_2,R2_4)
R0_6 = np.dot(R0_4,R4_6)

print(R0_6)