import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-5, 5])
ax.autoscale(enable=False)
position = 0
xVals = np.linspace(0,10,10)
yVals = np.zeros(xVals.shape)
scatterArtist = ax.scatter(xVals,yVals, facecolor='C0')



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
    global scatterArtist
    if (position >= len(xVals)):
        position = position-len(xVals)
    
    xVals[position%len(xVals)] = xVal
    yVals[position%len(yVals)] = yVal

    position+=1
    scatterArtist.remove()
    scatterArtist = ax.scatter(xVals, yVals, facecolor='C0')


cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()