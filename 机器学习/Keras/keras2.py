import pandas as pd

file = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

df1= pd.read_csv(file,header=None)

df1.to_csv('test.csv',index=False,header=None)