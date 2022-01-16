import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



fig, ax = plt.subplots()
plt.xlim([0, 10])
plt.ylim([-5, 5])
plt.autoscale(enable=False)
position = 0
xVals = np.linspace(0,10,10)
yVals = np.zeros(xVals.shape)
ax.scatter(xVals,yVals)



def onclick(event):

    addDotToPlot(event.xdata, event.ydata)
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    
    plt.show()

    
def addDotToPlot(xVal, yVal):
    global position
    global xVals
    global yVals
    global ax
    if (position >= len(xVals)):
        position = position-len(xVals)
    
    xVals[position%len(xVals)] = xVal
    yVals[position%len(yVals)] = yVal

    position+=1
    ax.clear()
    ax.scatter(xVals, yVals)


cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()