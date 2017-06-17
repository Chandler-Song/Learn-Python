import pandas as pd

#1
#定义资料集并打印出
# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                              'A': ['A0', 'A1', 'A2', 'A3'],
#                              'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                               'C': ['C0', 'C1', 'C2', 'C3'],
#                               'D': ['D0', 'D1', 'D2', 'D3']})
#
# print(left)
# print(right)
# #on：列名，join用来对齐的那一列的名字，
# # 用到这个参数的时候一定要保证左表和右表用来对齐的那一列都有相同的列名。
# res = pd.merge(left,right,on = 'key')
# print(res)
#______________________________________________________________________________
#2
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                       'key2': ['K0', 'K1', 'K0', 'K1'],
#                       'A': ['A0', 'A1', 'A2', 'A3'],
#                       'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                        'key2': ['K0', 'K0', 'K0', 'K0'],
#                        'C': ['C0', 'C1', 'C2', 'C3'],
#                        'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)
# #使用merge的时候可以选择多个key作为复合可以来对齐合并。
# #通过on指定数据合并对齐的列,默认how为inner
# #how = [ 'left','right','inner','outer']
# res = pd.merge(left,right,on = ['key1','key2'],how = 'left')
# print(res)
#______________________________________________________________________________
#3
#定义资料集并打印出
#v0.17.0 版本的pandas开始还支持一个indicator的参数，如果置True的时候，
# 输出结果会增加一列 ’ _merge’。_merge列可以取三个值
#left_only 只在左表中
#right_only 只在右表中
#both 两个表中都有
#直观地显示出以'how'方式merge后的结果在原始数据集中的存在情况
#如果indicator指定为'True'的话，则输出结果新增列名为'_merge',否则为indicator你所指定的值
# df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
# df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
# print(df1)
# print(df2)
# res = pd.merge(df1,df2,on = 'col1',how = 'outer',indicator = True)
# print(res)
#______________________________________________________________________________
#4
#定义资料集并打印出
# left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
#                      'B': ['B0', 'B1', 'B2']},
#                      index=['K0', 'K1', 'K2'])
# right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
#                       'D': ['D0', 'D2', 'D3']},
#                      index=['K0', 'K2', 'K3'])
#
# print(left)
# print(right)
# res = pd.merge(left,right,left_index = True,right_index = True,how = 'outer')
# #res = pd.merge(left,right,left_index = True,right_index = True,how = 'inner')
# print(res)
#______________________________________________________________________________
#5
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
#如果和表合并的过程中遇到有一列两个表都同名，但是值不同，
# 合并的时候又都想保留下来，就可以用suffixes给每个表的重复列名增加后缀。
res = pd.merge(boys,girls,on = 'k',suffixes = ['_boy','_girl'],how = 'outer')
print(res)