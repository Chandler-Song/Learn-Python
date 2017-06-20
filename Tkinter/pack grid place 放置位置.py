import tkinter as tk

window = tk.Tk()
window.title('My Window')
#窗口大小
window.geometry('200x200')


# Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，一下是Tkinter公开的几何管理类：包、网格、位置
# 几何方法	描述
# pack()	包装；
# grid()	网格；
# place()	位置；

#1. pack()
# tk.Label(window,text = 1).pack(side = 'top')
# tk.Label(window,text = 1).pack(side = 'bottom')
# tk.Label(window,text = 1).pack(side = 'left')
# tk.Label(window,text = 1).pack(side = 'right')

#2. grid()
# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text = 1).grid(row = i,column = j,padx = 10,
#                                        pady = 10)


#3. place()
# tk.Label(window,text = 1).place(x = 10,y=100,anchor = 'nw')

window.mainloop()