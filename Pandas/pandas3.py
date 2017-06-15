#encoding=utf-8
import numpy as np
import pandas as pd


def main():
    #Concat
    date = pd.date_range("20170301",periods=8)
    df = pd.DataFrame(np.random.randn(8,5),index = date,columns = list("ABCDE"))
    pieces =[df[:3],df[-3:]]
    print pd.concat(pieces)
    left = pd.DataFrame({"key":["x","y"],"value":[1,2]})
    right = pd.DataFrame({"key":["x","z"],"value":[3,4]})
    print "LEFT:",left
    print "RIGHT:",right
    print pd.merge(left,right,on="key",how="left")
    df1 = pd.DataFrame({"A":["a","b","c","b"],"B":list(range(4))})
    print df1.groupby("A").sum()

    #Reshape
    #Time Series
    t_exam = pd.date_range("20170301",periods = 10,freq = "S")
    print t_exam

    #Graph
    ts = pd.Series(np.random.randn(1000),index=pd.date_range("20170301",periods=1000))
    ts = ts.cumsum()
    from pylab import *
    ts.plot()
    show()

    #File
    df2 = pd.read_excel("pandas.xlsx")
    print df2
    df2.to_csv("test.csv")

if __name__ == "__main__":
        main()