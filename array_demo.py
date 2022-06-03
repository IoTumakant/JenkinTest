import numpy as np 
Array_1=np.array([[[1,2,3],[2,2,3],[3,2,3]],[[1,2,3],[2,2,3],[3,2,3]]]) 
print(Array_1.size) 
print(Array_1.shape) 
print(type(Array_1)) 
Array_1=Array_1+2 
print(Array_1) 
Array_2=np.full((3,3,3),'Umakant') 
Array_2[2][2][2]="Ramakant" 
print(Array_2) 
print(Array_1[1][2][2])
