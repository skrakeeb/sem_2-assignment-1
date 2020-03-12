'''
coded by: Rakeeb
coded for: solving linear equations using numpy.linalg.solve
'''

import numpy as np 

a= np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])
b= np.array([2,2,2])

x= np.linalg.solve(a,b)
print('the solution of the given set of equations: ',x)
