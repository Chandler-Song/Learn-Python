import tkinter as tk

window = tk.Tk()
window.title('My Window')
#窗口大小
window.geometry('200x200')
#输入控件；用于显示简单的文本内容
var1 = tk.StringVar()
l = tk.Label(window,bg = 'yellow',textvariable = var1,width = 4,)
l.pack()

def print_selection():
    #获取光标选中位置的值
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window,text='print selection',width = 15,height = 2,command = print_selection)
# 将小部件放置到主窗口中
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
#列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
lb = tk.Listbox(window,listvariable = var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

# 进入消息循环
window.mainloop()