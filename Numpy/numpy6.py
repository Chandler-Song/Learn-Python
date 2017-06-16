import numpy as np

#64：需要精确的话，16:可以忽略精度并且需要更多的空间来存储数据的话
a = np.array([2,23,4],dtype = np.int64)
b = np.empty((3,4))#非常接近于0的数字
#通过指定开始值、终值和步长创建表示等差数列的一维数组，注意得到的结果数组不包含终值
c = np.arange(10,20,2)
d = np.arange(12).reshape(3,4)
#通过指定开始值、终值和元素个数创建表示等差数列的一维数组，可以通过endpoint参数指定是否包含终值，默认值为True，即包含终值
e = np.linspace(1,10,6).reshape(2,3)
print (a.dtype)
print (b)
print (c)
print (d)
print (e)
