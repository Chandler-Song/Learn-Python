import tkinter as tk

window = tk.Tk()
window.title('My Window')
#窗口大小
window.geometry('200x200')
#输入控件；用于显示简单的文本内容
e = tk.Entry(window,show = None)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)


def insert_end():
    var = e.get()
    t.insert('end',var)

def insert_concrete():
    var = e.get()
    t.insert(1.1,var)

b1 = tk.Button(window,text='insert point',width = 15,height = 2,command = insert_point)
# 将小部件放置到主窗口中
b1.pack()
b2 = tk.Button(window,text='insert end',width = 15,height = 2,command = insert_end)
b2.pack()
b3 = tk.Button(window,text='insert concrete',width = 15,height = 2,command = insert_concrete)
b3.pack()
#文本控件；用于显示多行文本
t = tk.Text(window,height = 2)
t.pack()
# 进入消息循环
window.mainloop()