import tkinter as tk

window = tk.Tk()
window.title('My Window')
#窗口大小
window.geometry('200x200')

l = tk.Label(window,bg = 'yellow',width = 20,text = 'empty')
l.pack()

def print_selection(v):
    l.config(text = 'you have selected ' + v)

s = tk.Scale(window,labe='try me',from_ = 5,to = 11,orient = tk.HORIZONTAL,length = 200
             ,showvalue = 0,tickinterval = 3,resolution = 0.01,command = print_selection)
s.pack()

# 进入消息循环
window.mainloop()