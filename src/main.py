import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from playsound import playsound
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

#actions to perform on click onto axes/figure?
def onclick(event):
    #spawn the a firework at click
    FireworkManager.spawnNewFirework(event.xdata, event.ydata)
    


def continueFireworks(frameNumber):
    #update the position of the firework particles
    FireworkManager.drawFireworks(ax)

cid = fig.canvas.mpl_connect('button_press_event', onclick)
animation = FuncAnimation(fig, continueFireworks, interval=40)
plt.show()