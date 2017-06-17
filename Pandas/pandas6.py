import pandas as pd
import numpy as np

# #concatenating
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
# print(df1)
# print(df2)
# print(df3)
# #垂直方向合并,忽略原有index
# res = pd.concat([df1,df2,df3],axis = 0,ignore_index = True)
# print(res)
#join,['inner','outer']
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])
# print(df1)
# print(df2)
# #如果为’inner’得到的是两表的交集，如果是outer，得到的是两表的并集
# res = pd.concat([df1,df2],join = 'inner',ignore_index = True)
# print(res)
#如果有join_axes的参数传入，可以指定根据那个轴来对齐数据
#例如根据df1表对齐数据，就会保留指定的df1表的轴，然后将df2的表与之拼接
# 依据对应的轴，df2没有的，则以缺失值NaN表示
#如果不指定join_axes，则会以并集的形式都展现出来
# res = pd.concat([df1,df2],axis = 1,join_axes = [df1.index])
# print(res)

#定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])

#默认沿着列进行拼接（axis = 0，列对齐）
res = df1.append([df2,df3],ignore_index = True)
print(res)

s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1.append(s1,ignore_index = True)
print(res)