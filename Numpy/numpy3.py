#--coding:utf-8--
import numpy as np

#数据类型单一，运算速度快
#均值为1.75，标准差为0.20，生成长度为5000的符合正太分布的随机数并以保留两位小数的形式四舍五入
height = np.round(np.random.normal(1.75,0.20,5000),2)
weight =  np.round(np.random.normal(60.32,15,5000),2)

#列组合
np_city = np.cloumn_stack((height,weight))

#返回数组元素平均值
print np.mean(np_city[:,0])
#找到数组中的中位数(中间两个数的平均值)
print np.median(np_city[:,0])
#求数组中变量之间的相关性
print np.corrcoef(np_city[:,0],np_city[:,1])
#计算矩阵标准差
print np.std(np_city[:,0])



