import tkinter as tk

window = tk.Tk()
window.title('My Window')
#窗口大小
window.geometry('200x200')

def moveit():
    canvas.move(rect,0,2)


#画布控件；显示图形元素如线条或文本
canvas = tk.Canvas(window,bg = 'blue',height = 250,width = 500)
image_file = tk.PhotoImage(file='test.gif')
image = canvas.create_image(10,10,anchor = 'nw',image = image_file)
x0,y0,x1,y1 = 50,50,80,80
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start = 0,extent = 180)
rect = canvas.create_rectangle(100,30,100+20,30+20)
canvas.pack()
b = tk.Button(window,text = 'move',command = moveit).pack()


# 进入消息循环
window.mainloop()