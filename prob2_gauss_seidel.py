'''
coded by: Rakeeb
code for:
'''

import numpy as np 

x_exact= np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])

a= np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b= np.array([1,2,3,4,5])

# Gauss Seidel method:

x= np.array([0,0,0,0,0])

U= np.triu(a,k=1) #upper triangular part of "a" without main diagonal
D_L= np.tril(a,k=0) #lower triangular part of "a" with the main diagonal
'''
As was done in class, U is the upper triangular part and D_L is the (D+L) matrix, where D is the diagonal part
 and L is the lower triangular part of the given matrix. We have to take the inverse of the (D+L) part and 
 multiply it to the right hand side.
'''

D_L_inv= np.linalg.inv(D_L)

i=0
while (any(np.abs(x_exact[j]-x[j])>0.01 for j in range (5))):
	s= b-np.matmul(U,x)
	x= np.matmul(D_L_inv,s)
	i=i+1
print('solution by Gauss-Seidel method: ',x ,'\nNumber of  itarations needed: ',i )		
