'''
coded by: Rakeeb
code for:
'''

import numpy as np 

x_exact= np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])

a= np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b= np.array([1,2,3,4,5])

#jacobi method:

x= np.array([0,0,0,0,0])

d= np.diag(np.diag(a))  #making a diagonal matix with elements same as the diagonal of "a".
a_new= a- d
'''
As was done in class here "d" is the diagonal matrix containing only diaginal elements of "a" 
and "a_new" is the (L+U) matrix, where L is the lower triangular and U is the upper triangular part of the given matrix.
We have to take the inverse of D in the right hand side.
'''
d_inv= np.linalg.inv(d)

i=0
while (any(np.abs(x_exact[j]-x[j])>0.01 for j in range (5))):
	s= b-np.matmul(a_new,x)
	x= np.matmul(d_inv,s)
	i=i+1
print('solution by Jacobi method: ',x ,'\nNumber of  itarations needed: ',i )	

