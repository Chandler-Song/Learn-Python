import numpy as np


a = np.random.random((2,4))
print (np.sum(a))
print (a.sum())
#axis=0表述列
#axis=1表述行
print (a,a.sum(axis = 1))
print (a,a.sum(axis = 0))

print (np.min(a))
print (a.min(axis=0))
print (np.max(a))
print (a.max())

