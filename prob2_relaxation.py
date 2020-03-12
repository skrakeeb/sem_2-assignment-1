'''
coded by : Rakeeb
coded for: study of Q-R decomposition
'''

#can't find why this code is going in infinite loop.


import numpy as np 

x_exact= np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])

a= np.array([[0.2,0.1,1,1,0.0],[0.1,4,-1,1,-1],[1,-1,60,0.0,-2],[1,1,0,8,4],[0.0,-1,-2,4,700]])
b= np.array([1,2,3,4,5])

# relaxation method:

x= np.array([0,0,0,0,0])
r= np.array([0,0,0,0,0])
w= 1.25      

i=0
while (any(np.abs(x_exact[j]-x[j])> 0.01 for j in range (5))):
	for k in range(5):
		r[k]= b[k]-np.dot(a[k],x)  #the residual vector

		x[k]= x[k]+ w*(r[k]/a[k][k]) #updated solution vector

	i=i+1
	
print('solution by relaxation  method: ',x ,'\nNumber of  itarations needed: ',i )		

