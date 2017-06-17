import numpy as np
import pandas as pd


dates = pd.date_range('20130101',periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index = dates,columns=['A','B','C','D'])

print(df['A'])
print(df.A)
print(df[0:3])
print(df['20130102':'20130104'])

#select by label:loc通过标签切片
##print(df.loc['20130102'])
print(df.loc['20130102',['A','B']])
#通过位置切片
print(df.iloc[[1,3,5],1:3])
#mixed selection:ix通过标签和位置进行混合筛选
print(df.ix[:3,['A','C']])
#Boolean indexing
print(df)
print(df.loc['20130104']['B'])
df.loc['20130104']['B']=7
print(df.loc['20130104']['B'])
print(df.A>8)
print(df[df.A > 8])
