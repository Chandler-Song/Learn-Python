import tkinter as tk

window = tk.Tk()
window.title('My Window')
#窗口大小
window.geometry('200x200')

tk.Label(window,text = 'on the window').pack()
#框架控件；在屏幕上显示一个矩形区域，多用来作为容器
frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm,)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l,text = 'on the frm_l1').pack()
tk.Label(frm_l,text = 'on the frm_l2').pack()
tk.Label(frm_r,text = 'on the frm_r').pack()

window.mainloop()