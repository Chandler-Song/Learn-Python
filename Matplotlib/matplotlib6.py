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
# x = np.linspace(-1,1,50)
# y1 = 2 * x + 1
# y2 = x**2
# plt.figure()
# plt.plot(x,y1)
# #指定figure窗口号为3，窗口长宽分别为8,5
# plt.figure(num=3,figsize = (8,5))
# plt.plot(x,y2)
# #color指定线的颜色,linewidth指定线宽,linesyle指定线的类型
# plt.plot(x,y1,color = 'red',linewidth = 1.0,linestyle = '--')
# #设置坐标轴的范围
# plt.xlim((-1,2))
# plt.ylim((-2,3))
# #描述x轴
# plt.xlabel('I am x')
# #描述y轴
# plt.ylabel('I am y')
#
# new_ticks = np.linspace(-1,2,5)
# print(new_ticks)
# #xticks 设置x轴间隔
# plt.xticks(new_ticks)
# #yticks将y轴坐标转换成指定内容
# #通过 r'$...$' 改变字体,通过转义符可以将\alpha转换成α
# plt.yticks([-2,-1.8,-1,1.22,3,],[r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
#
# #gca = 'get current axis'获取当前axes
# ax = plt.gca()
# #消除右边的轴以及上边的轴
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# #将x轴和y轴移动至0刻度处
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data',0))#outward,axes
# ax.spines['left'].set_position(('data',0))
# plt.show()
#____________________________________________________________________
#3 Legend 图例
# x = np.linspace(-1,1,50)
# y1 = 2 * x + 1
# y2 = x**2
# plt.figure()
#
# #设置坐标轴的范围
# plt.xlim((-1,2))
# plt.ylim((-2,3))
# #描述x轴
# plt.xlabel('I am x')
# #描述y轴
# plt.ylabel('I am y')
#
# new_ticks = np.linspace(-1,2,5)
# print(new_ticks)
# #xticks 设置x轴间隔
# plt.xticks(new_ticks)
# #yticks将y轴坐标转换成指定内容
# #通过 r'$...$' 改变字体,通过转义符可以将\alpha转换成α
# plt.yticks([-2,-1.8,-1,1.22,3,],[r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
#
# l1, = plt.plot(x,y2,label = 'up')
# #color指定线的颜色,linewidth指定线宽,linesyle指定线的类型
# l2, = plt.plot(x,y1,color = 'red',linewidth = 1.0,linestyle = '--',label = 'down')
# #三个最重要的必要参数
# # parent --- legend的父artist， 包含legend的对象
# #        比如用ax.legend()调用之后
# #        >>> print ax.get_legend().parent
# #        Axes(0.125,0.1;0.775x0.8)
# # handles --- 图例上面画出的各个artist（lines, patches）
# # labels --- artist 对应的标签
# #handle:The original object which is used to generate an appropriate entry in the legend.
# plt.legend(handles = [l1,l2,],labels = ['aaa','bbb'] ,loc = 'best')
#
# plt.show()
#____________________________________________________________________
#4 Annotation 注解
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0,y0,s=50,color = 'b')
plt.plot([x0,x0],[y0,0],'k--',lw = 2.5)

#method 1
#################
#method 1
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords = 'data',xytext = (+30,-30),textcoords = 'offset points',
             fontsize = 16,arrowprops = dict(arrowstyle = '->',connectionstyle = 'arc3,rad = .2'))

#method 2
plt.text(-3.7,3,r'$This\ is\ the\ some\ test.\ \mu\ \sigma_i\ \alpha_t$',fontdict = {'size':16,'color':'r'})
plt.show()