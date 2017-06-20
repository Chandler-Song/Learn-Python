import tkinter as tk
#用于显示你应用程序的消息框。
import tkinter.messagebox as ms

window = tk.Tk()
window.title('My Window')
#窗口大小
window.geometry('200x200')


def hit_me():
    pass
    # ms.showinfo(title = 'Hi',message = 'hahaha')
    # ms.showwarning(title = 'Hi',message = 'nonono')
    # ms.showerror(title = 'Hi',message = 'No!! never')
    # return 'yes' or 'no'
    # print(ms.askquestion(title = 'Hi',message = 'hahahaha'))
    #return 'True' or 'False'
    # print(ms.askyesno(title = 'Hi',message = 'hahahaha'))
    # print(ms.askokcancel(title = 'Hi',message = 'hahahaha'))


tk.Button(window,text = 'hit me',command = hit_me).pack()
window.mainloop()