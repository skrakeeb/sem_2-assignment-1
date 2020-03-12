'''
coded by: Rakeeb
coded for: to evaluate singular value decomposition of a given matrix and to match with 
           that obtaine dfrom numpy.linalg.svd
'''
import numpy as np 
import time

start1= time.time()  #initialising time
a= np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])

u,s,v= np.linalg.svd(a)

print('singular values obtained form np.linalg.svd:\n ',s)
print(f'Time taken for numpy.linalg.svd code : {time.time() - start1}')

start2= time.time()
a_trans = np.transpose(a)  #taking transpose
sq_mat= np.matmul(a_trans,a)  #making the square matrix A(transpose)*A
print('the square matrix made from "a": \n',sq_mat)
eig_v,eig_vec= np.linalg.eig(sq_mat)# determining eigen values and eigen vectors
evaluated_s= np.sqrt(eig_v) # taking the square root of the eigen values
print('evaluated singular values: ',evaluated_s)
print(f'Time taken for my code : {time.time() - start2}')
print('\n The numpy code is taking almost same time although they also calculated u and v.')
