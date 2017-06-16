import numpy as np

A = np.arange(3,15).reshape(3,4)
print(A)
#查找第一列所有元素
print(A[:,1])
#查找第一行所有元素
print(A[1,:])
#:左闭右开
print(A[1,:-1])

#通过转置转迭代行为列
for column in A.T:
    print(column)

#numpy.flatten()返回一份拷贝，对拷贝所做的修改不会影响（reflects）原始矩阵
print(A.flatten())
#如果想对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
for item in A.flat:
    print(item,end=' ')
