import numpy as np

A = np.arange(12).reshape((3,4))
print(A)
#split如果不等量的分割会报错
#沿着水平的轴分割成2块
print(np.split(A,2,axis = 1))
#沿着垂直的轴分割成3块
print(np.split(A,3,axis = 0))
#array_split:功能与split一样，唯一的区别是 array_split allows indices_or_sections to be an integer that does not equally divide the axis.
print(np.array_split(A,3,axis=1))
#水平分割：hsplit;垂直分割:vsplit
print(np.hsplit(A,2))
print(np.vsplit(A,3))