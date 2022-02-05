from re import X
import matplotlib.lines as mpl
import numpy as np
import threading
from playsound import playsound
from fireworks.fireworkParticles import FireworkParticles

'''
Class that manages all the fireworks

It will hold all the fireworks, draw all the fireworks, etc.'''
class FireworkManager:

    fireworks = np.array( [FireworkParticles(-100,0) for i in range(10)],
                    dtype=object)

    fireworkLoadPosition = 0

    fireworksArtisits = np.array([None for i in range (len(fireworks))],
                    dtype=object)

    
    def generateColors(fireworks):
        numberFireworks = len(fireworks)
        randArr=np.random.rand((3*numberFireworks))
        colors =[tuple(randArr[3*x:3*x+3]) for x in range(len(randArr)//3)]
        return colors
    
    colors = generateColors(fireworks)

    @staticmethod
    def playFireworkSound(name):
        playsound('./media/sound/fireworkASound.mp3')
    
    @staticmethod
    def spawnNewFirework(xVal, yVal):
        pos = FireworkManager.fireworkLoadPosition
        if (pos >= len(FireworkManager.fireworks)):
            FireworkManager.fireworkLoadPosition = pos-len(FireworkManager.fireworks)
            pos = FireworkManager.fireworkLoadPosition

        #add in a new firework
        FireworkManager.spawnFirework(pos, xVal, yVal)

        #increment the position of the next firework to swap out
        FireworkManager.fireworkLoadPosition+=1

        #make the popping sound
        x = threading.Thread(target=FireworkManager.playFireworkSound, args=(1,))
        x.start()


    # updates the position of all fireworks particles
    @staticmethod
    def updateFireworks():
        for firework in FireworkManager.fireworks:
            firework.update()

    '''
    Replaces the nth firework with a new firewok as a designated location

    @param n The nth firework that gets replaced
        Perhaps we should have n internal to the firework manager...
    @param xVal The x position for the firework
    @param yVal The y position for the firework
    '''
    @staticmethod
    def spawnFirework(n, xVal, yVal):
        FireworkManager.fireworks[n] = FireworkParticles(xVal,yVal)

    '''
    Draws the fireworks to an axes
    
    @param ax Matplotlib axes'''
    @staticmethod
    def drawFireworks(ax):
        #get the positions of the fireworks.
        #yo, let's not even do this update step in the draw step
        FireworkManager.updateFireworks()
        #erase the dots of yester-Frame
        if FireworkManager.fireworksArtisits[0] is not None:
            FireworkManager.eraseArtists()
        #iterate through all the fireworks so that we can have one artist
        #per firework
        i = 0
        for firework in FireworkManager.fireworks:
            if (not firework.isDead()):
                xFirework = firework.particlesX
                yFirework = firework.particlesY
                FireworkManager.fireworksArtisits[i] = ax.scatter(
                    xFirework, yFirework, facecolor=FireworkManager.colors[i])
            else:
                xFirework = np.empty(1)
                xFirework.fill(-1)
                yFirework = np.empty(1)
                xFirework.fill(-1)
                FireworkManager.fireworksArtisits[i] = ax.scatter(
                    xFirework, yFirework, facecolor=FireworkManager.colors[i])
            i += 1


    '''
    Erases the firework artists
    
    '''
    @staticmethod
    def eraseArtists():
        for artist in FireworkManager.fireworksArtisits:
            if artist is not None:
                artist.remove()