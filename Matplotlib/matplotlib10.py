import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

fig,ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def animation(i):
    line.set_ydata(np.sin(x+i/10))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = ani.FuncAnimation(fig = fig,func=animation,frames=100,init_func=init,interval = 20,blit = False)
plt.show()