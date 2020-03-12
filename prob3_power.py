'''
coded by: Rakeeb
coded for: Study of power method
'''


import numpy as np 

a= np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
x= np.array([1,50,0])
y= np.array([1,1,1])

eigv,eigvec= np.linalg.eigh(a) # determining eigen value and eigen vectors by numpy functions

max_mod_ev= np.amax(abs(eigv)) #picking maximum modulus eigenvalue
print('maximum absolute eigenvalue: ',max_mod_ev) 

n=1
error=5  #taking an arbitrary error in percentage
while error > 1 :
	a_n= np.linalg.matrix_power(a,n)
	a_n1= np.linalg.matrix_power(a,n+1)
	x1= np.matmul(np.matmul(a_n1,x),y)
	x2= np.matmul(np.matmul(a_n,x),y)
	ev_pow= float(x1)/float(x2)     #determining eigen value by power method
	error= abs((max_mod_ev-abs(ev_pow)))*100/max_mod_ev   #error from exact value in percentage.
	n=n+1

print('eigen value by power method: ',ev_pow)
