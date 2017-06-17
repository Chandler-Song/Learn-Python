import numpy as np
import pandas as pd


dates = pd.date_range('20130101',periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index = dates,columns=['A','B','C','D'])

# df.iloc [2,2] = 1111
# df.loc['20130101','B'] = 2222
# df.A[df.A>4] = 0
# df['F'] = np.nan
# df['E'] = pd.Series([1,2,3,4,5,6],index = pd.date_range('20130101',periods = 6))
# print(df)

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
#检测dataframe中哪个位置为缺失数据
print(df.isnull())
#检测是否包含缺失数据
print(np.any(df.isnull()) == True)
#当数据中存在NaN缺失值时，我们可以用其他数值替代NaN
print(df.fillna(value = 0))

#any axis=0只要一行中有一个nan,就删除这行
#all axis=0当且仅当一行中的所有值都为nan时才删除该行
print(df.dropna(axis = 0,how = 'any'))#how = {'any','all'}
