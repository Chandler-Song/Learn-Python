#--coding:utf-8--
import numpy as np
import matplotlib.pyplot as plt

#折线图
# year = [1950,1970,1990,2010]
# pop = [2.519,3.692,5.263,6.972]
# plt.plot(year,pop)

#散点图
# n = 1024
# X = np.random.normal(0,1,n)
# Y = np.random.normal(0,1,n)
# T = np.arctan2(Y,X) #for color value
# # plt.scatter(X,Y,s = 75,c = T,alpha = 0.5)
# plt.scatter(np.arange(5),np.arange(5))
# plt.xlim((-1.5,1.5))
# plt.ylim((-1.5,1.5))
# plt.xticks(())
# plt.yticks(())
# plt.scatter(year,pop)

#柱状图
# import matplotlib.pyplot as plt
# import numpy as np
#
# n = 12
# X = np.arange(n)
# Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
#
# plt.bar(X, +Y1,facecolor = '#9999ff',edgecolor = 'white')
# plt.bar(X, -Y2,facecolor = '#ff9999',edgecolor = 'white')
#
# for x,y in zip(X,Y1):
#     #ha: horizontal alignment
#     plt.text(x + 0.4,y + 0.05,'%.2f'%y,ha = 'center',va = 'bottom')
#
# for x,y in zip(X,Y2):
#     #ha: horizontal alignment
#     plt.text(x + 0.4,-y - 0.05,'-%.2f'%y,ha = 'center',va = 'top')
#
#
# plt.xlim(-.5, n)
# plt.xticks(())
# plt.ylim(-1.25, 1.25)
# plt.yticks(())

#等高线图
# import matplotlib.pyplot as plt
# import numpy as np
#
# def f(x,y):
#     # the height function
#     return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
#
# n = 256
# x = np.linspace(-3, 3, n)
# y = np.linspace(-3, 3, n)
# #将x,y绑定成网格的输入值
# X,Y = np.meshgrid(x, y)
# plt.contourf(X,Y,f(X,Y),8,alpha = 0.75,cmap = plt.cm.hot)
#
# C = plt.contour(X,Y,f(X,Y),8,colors = 'black',linewidth = .5)
# plt.clabel(C,inline = True,fontsize = 10)
# plt.xticks(())
# plt.yticks(())
# plt.show()
#image
# import matplotlib.pyplot as plt
# import numpy as np
#
# a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
#               0.365348418405, 0.439599930621, 0.525083754405,
#               0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
# plt.imshow(a,interpolation = 'nearest',cmap = 'bone',origin = 'upper')
# plt.colorbar(shrink = 0.9)
#
# plt.xticks(())
# plt.yticks(())
#3D image
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# # X, Y value
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
# R = np.sqrt(X ** 2 + Y ** 2)
# # height value
# Z = np.sin(R)
#
# ax.plot_surface(X,Y,Z,rstride = 1,cstride = 1,cmap = plt.get_cmap('rainbow'))
# ax.contourf(X,Y,Z,zdic = 'z',offset = -4,cmap = 'rainbow')
# ax.set_zlim(-2,2)
# plt.show()

#subplot
# plt.figure()
# plt.subplot(2,1,1)
# plt.plot([0,1],[0,1])
# plt.subplot(2,3,4)
# plt.plot([0,1],[0,2])
# plt.subplot(235)
# plt.plot([0,1],[0,3])
# plt.subplot(236)
# plt.plot([0,1],[0,4])
import matplotlib.gridspec as gridspec
##method1: subplot2grid
# plt.figure()
# ax1 =plt.subplot2grid((3,3),(0,0),colspan = 3,rowspan  = 1)
# ax1.plot([1,2],[1,2])
# ax1.set_title('ax1_title')
# ax2 =plt.subplot2grid((3,3),(1,0),colspan = 2)
# ax3 =plt.subplot2grid((3,3),(1,2),rowspan = 2)
# ax4 =plt.subplot2grid((3,3),(2,0))
# ax5 =plt.subplot2grid((3,3),(2,1))
##method2: gridspec
# plt.figure()
# gs = gridspec.GridSpec(3,3)
# ax6 = plt.subplot(gs[0,:])
# ax7 = plt.subplot(gs[1,:2])
# ax8 = plt.subplot(gs[1:,2])
# ax9 = plt.subplot(gs[-1,0])
# ax10 = plt.subplot(gs[-1,-2])
##method3: easy to define structure
# f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex= True,sharey = True)
# ax11.scatter([1,2],[1,2])
# plt.tight_layout()
# plt.show()
