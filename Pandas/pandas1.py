import pandas as pd
import numpy as np
#NAN is nan (不合法的值)
print (np.nan is np.NAN)
#Series 是一个一维数组结构的，可以存入任一一种python的数据类型(integers, strings, floating point numbers, Python objects, etc.)。
s = pd.Series([1,3,6,np.nan,44,1])
print(s)
#生成自‘20160101'开始的6个datetime
dates  = pd.date_range('20160101',periods = 6)
print(dates)

#index:行名，columns:列名
df = pd.DataFrame(np.random.randn(6,4),index = dates,columns = ['a','b','c','d'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

df2 = pd.DataFrame({'A':1.,'B':pd.Timestamp('20130102'),'C':pd.Series(1,index = list(range(4)),dtype = 'float32'),
                    'D':np.array([3]*4,dtype = 'int32'),'E':pd.Categorical(['test','train',
                    'test','train']),'F':'foo'})
print(df2)
print(df2.dtypes)
#打印出行标
print(df2.index)
#打印出列标
print(df2.columns)
#打印出值
print(df2.values)
#  describe()函数对于数据的快速统计汇总：
# dataFrame.describe()，会统计出各列的：计数，平均数，方差，最小值，最大值，以及quantile数值
print(df2.describe())
#转置矩阵
print(df2.T)
#对行标进行降序排序
print(df2.sort_index(axis = 1,ascending = False))
#对'E'列值进行排序
print(df2.sort_values(by='E'))


