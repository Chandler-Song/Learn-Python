import tkinter as tk

window = tk.Tk()
window.title('My Window')
#窗口大小
window.geometry('200x100')
#StringVar是可变字符串，get()和set()是得到和设置其内容
var = tk.StringVar()
#标签控件；可以显示文本和位图
#使用 textvariable 替换 text, 因为这个可以变化
l = tk.Label(window,textvariable = var,bg = 'green',font=('Arial',12),
             width = 15,height = 2 )
l.pack()
# l.place()
on_hit = False
def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

#按钮控件；在程序中显示按钮。
b = tk.Button(window,text='hit me',width = 15,height = 2,command = hit_me)
# 将小部件放置到主窗口中
b.pack()
# 进入消息循环
window.mainloop()