import numpy as np

A = np.arange(2,14).reshape((3,4))

#返回最值所在的索引（下标）
print(np.argmin(A))
print(np.argmax(A))
#均值
print(A.mean())
print(np.average(A))
#中位数
print(np.median(A))
#累加
print(np.cumsum(A))
#返回相邻数组元素的差值构成的数组
print(np.diff(A))
#nonzeros(a)返回数组a中值不为零的元素的下标，它的返回值是一个长度为a.ndim(数组a的轴数)的元组，元组的每个元素都是一个整数数组，其值为非零元素的下标在对应轴上的值。
print(np.nonzero(A))
#排序
A.sort()
print (A)
#反转
print(np.transpose(A))
print(A.T.dot(A))
#会给出一个区间，在区间之外的数字将被剪除到区间的边缘，例如给定一个区间[0,1]，则小于0的
#将变成0，大于1则变成1.
print(np.clip(A,5,9))