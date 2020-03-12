'''
coded by : Rakeeb
coded for: study of Q-R decomposition
'''


import  numpy as np 

a= np.array([[5,-2],[-2,8]])



eig_v,eig_vec= np.linalg.eigh(a)
print('eigen values by numpy function: ',eig_v)

while abs(a[0][1]) >0.00001 or abs(a[1][0]) >0.00001 :
	q,r=np.linalg.qr(a)
	a=np.dot(r,q)  # as done in class in every step the new matrix is RQ till it becomes diagonal. 

print('eigen values by Q-R decomposition: ',np.diag(a))

