import matplotlib.pyplot as plt
import numpy as np
#1
#linspace()通过指定开始值、
# 终值和元素个数创建表示等差数列的一维数组，可以通过endpoint参数指定是否包含终值，默认值为True，即包含终值。
# x = np.linspace(-1,1,50)
# # y = 2 * x + 1
# y = x**2
# plt.plot(x,y)
# plt.show()
#____________________________________________________________________
#2 Figure
#一个Figure对象可以包含多个子图(Axes)
x = np.linspace(-1,1,50)
y1 = 2 * x + 1
y2 = x**2
plt.figure()
plt.plot(x,y1)
#指定figure窗口号为3，窗口长宽分别为8,5
plt.figure(num=3,figsize = (8,5))
plt.plot(x,y2)
#color指定线的颜色,linewidth指定线宽,linesyle指定线的类型
plt.plot(x,y1,color = 'red',linewidth = 1.0,linestyle = '--')
#设置坐标轴的范围
plt.xlim((-1,2))
plt.ylim((-2,3))
#描述x轴
plt.xlabel('I am x')
#描述y轴
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
#xticks 设置x轴间隔
plt.xticks(new_ticks)
#yticks将y轴坐标转换成指定内容
#通过 r'$...$' 改变字体,通过转义符可以将\alpha转换成α
plt.yticks([-2,-1.8,-1,1.22,3,],[r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
plt.show()