import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from fireworks.fireworkManager import FireworkManager


#The firework that we are currently modifying
fireworkPosition = 0
#^^Move this into the firework manager...

# CREATING THE PLOT AND PARAMS
fig, ax = plt.subplots()
#set the length of the axis
ax.set_xlim([0, 10])
ax.set_ylim([-5, 5])
ax.autoscale(enable=False)


def onclick(event):
    addFirework(event.xdata, event.ydata)
    plt.show()

def addFirework(xVal,yVal):
    global fireworkPosition
    global ax
    global fireworkArtist
    if (fireworkPosition >= FireworkManager.getNumFireworks()):
        fireworkPosition = fireworkPosition-FireworkManager.getNumFireworks()
    #add in a new firework
    FireworkManager.spawnFirework(fireworkPosition, xVal, yVal)

    #increment the position of the next firework to swap out
    fireworkPosition+=1
    #draw all fireworks to the axes
    FireworkManager.drawFireworks(ax)


cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()