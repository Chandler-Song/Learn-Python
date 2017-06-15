#encoding=utf-8
import numpy as np

def main():
    #1
    lst = [[1,3,5],[2,4,6]]
    np_lst = np.array(lst)
    print type(np_lst)
    #数组的维度几行几列
    print np_lst.shape
    # 给出数组的尾数或数组的轴数
    print np_lst.ndim
    np_lst=np.array(np_lst,dtype=float)
    #创建数组的数据类型
    print np_lst.dtype
    #数组中元素在内存中所占字节数
    print np_lst.itemsize
    # 数组中元素的个数
    print np_lst.size

    #2 Some Arrays
    #生成2行4列的全0矩阵
    print np.zeros([2,4])
    #生成3行5列的全1矩阵
    print np.ones([3,5])
    print "Random:"
    #生成2行4列的0~1之间的随机数矩阵
    print np.random.rand(2,4)
    #生成一个0~1之间的随机数
    print np.random.random()
    print "RandInt:"
    #生成3个1到10之间的一个随机整数
    print np.random.randint(1,10,3)
    print "Randomn:"
    #生成2行1列标准正太分布下的随机数矩阵
    print np.random.randn(2,1)
    print "Choice:"
    #从指定数字中随机生成其中的某个数字
    print np.random.choice([10,20,30])
    print "Distribute:"
    print np.random.beta(1,10,100)
    #3 Array Opes
    #生成1~10的numberArray(左闭右开)
    test = np.arange(1,11).reshape([2,-1])
    print test
    print np.exp(test)
    print np.exp2(test)
    print np.sqrt(test)
    print np.sin(test)
    print np.log(test)#自然底数

    test = np.array([[[1,2,3,4],[4,5,6,7]],[[7,8,9,10],[10,11,12,13]],[[14,15,16,17],[18,19,20,21]]])
    print test.sum(axis=1)
    print test.max()
    lst1 = np.array([10,20,30,40])
    lst2 = np.array([4,3,2,1])
    print lst1 + lst2
    print lst1 * lst2
    print lst1 / lst2
    print lst1**2
    print np.dot(lst1.reshape([2,2]),lst2.reshape([2,2]))
    print np.concatenate((lst1,lst2),axis = 0)
    print np.vstack((lst1,lst2))
    print np.hstack((lst1,lst2))
    print np.split(lst1,2)
    print np.copy(lst1)

    #4 liner
    from numpy.linalg import *
    #生成单位矩阵
    print np.eye(3)
    lst = np.array([[1.,2.],[3.,4.]])
    print "Inv:"
    #生成逆矩阵
    print inv(lst)
    print "T:"
    #生成反置矩阵
    print lst.transpose()
    #生成行列式
    print "Det:"
    print det(lst)
    #生成特征向量
    print eig(lst)
    y = np.array([[5.],[7.]])
    print "Solve"
    print solve(lst,y)

    #5 others
    print "FFT"
    print np.fft.fft(np.array([1,1,1,1,1,1,1,1]))
    print "Coef:"
    print np.corrcoef([1,0,1],[0,2,1])
    print "Poly:"
    print np.poly1d([2,1,3])

if __name__ == "__main__":
    main()