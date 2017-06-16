import numpy as np

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
#垂直组合数组a和数组b
C=np.vstack((A,B))#vertical stack
#水平组合数组a和数组b
D=np.hstack((A,B))#horizontal stack
#可以以指定axis的方式合并多个array
E=np.concatenate((A,B,B,A),axis = 0)
print(D)
print(A.shape,C.shape,D.shape)
#插入维度
# print(A[np.newaxis,:].shape)
# print(A[:,np.newaxis].shape)
print(E)
