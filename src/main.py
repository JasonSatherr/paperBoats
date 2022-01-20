import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from fireworks.fireworkManager import FireworkManager


#xValues of the plotted dots
xVals = np.linspace(0,10,10)
#yValues of the plotted dots
yVals = np.zeros(xVals.shape)
#position in the array
position = 0
fireworkPosition = 0

# CREATING THE PLOT AND PARAMS
fig, ax = plt.subplots()
#set the length of the axis
ax.set_xlim([0, 10])
ax.set_ylim([-5, 5])
ax.autoscale(enable=False)
#set the color of the dots in the axes
scatterArtist = ax.scatter(xVals,yVals, facecolor='C0')

#xpositions for firework particles
xFireworks, yFireworks = FireworkManager.getParticlePositions()
fireworkArtist = ax.scatter(xFireworks,yFireworks, facecolor='.5')

def onclick(event):

    addDotToPlot(event.xdata, event.ydata)
    addFirework(event.xdata, event.ydata)
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    
    plt.show()

def addFirework(xVal,yVal):
    global fireworkPosition
    global ax
    global fireworkArtist
    if (fireworkPosition >= FireworkManager.getNumFireworks()):
        fireworkPosition = fireworkPosition-FireworkManager.getNumFireworks()
    #add in a new firework
    FireworkManager.spawnFirework(fireworkPosition, xVal, yVal)
    xFireworks, yFireworks = FireworkManager.getParticlePositions()
    print(xFireworks)
    #update position of the firework particles
    #move out of this function...
    FireworkManager.updateFireworks()
    fireworkPosition+=1
    fireworkArtist.remove()
    xFireworks, yFireworks = FireworkManager.getParticlePositions()
    fireworkArtist = ax.scatter(xFireworks, yFireworks, facecolor='.5')

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