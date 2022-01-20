from re import X
import matplotlib.lines as mpl
import numpy as np
from fireworks.fireworkParticles import FireworkParticles


class FireworkManager:

    fireworks = np.array( [FireworkParticles(-100,0) for i in range(10)],
                    dtype=object)

    fireworksArtisits = np.array([None for i in range (len(fireworks))],
                    dtype=object)

    
    def generateColors(fireworks):
        numberFireworks = len(fireworks)
        randArr=np.random.rand((3*numberFireworks))
        colors =[tuple(randArr[3*x:3*x+3]) for x in range(len(randArr)//3)]
        print(type(colors[0]))
        return colors
    
    colors = generateColors(fireworks)
    

    # updates the position of all fireworks particles
    @staticmethod
    def updateFireworks():
        for firework in FireworkManager.fireworks:
            firework.update()

    # updates the position of all fireworks particles
    @staticmethod
    def getNumFireworks():
        return len(FireworkManager.fireworks)
    '''
    Replaces the nth firework with a new firewok as a designated location

    @param n The nth firework that gets replaced
        Perhaps we should have n internal to the firework manager...
    @param xVal The x position for the firework
    @param yVal The y position for the firewor
    '''
    @staticmethod
    def spawnFirework(n, xVal, yVal):
        FireworkManager.fireworks[n] = FireworkParticles(xVal,yVal)

    '''
    Returns a tuple with ALL x and y particle positions.

    Returns a tuple with the first element being an np array holding all X
    positions of the particles.  The second elemnt of the tuple is an array
    holding all Y positions of the particles.
    '''
    @staticmethod
    def getParticlePositions()->tuple:
        xArr = FireworkManager.getXFireworks()
        yArr =  FireworkManager.getYFireworks()
        return xArr, yArr

    '''
    Returns a numpy array of the x positions of all fireworks particles.
    '''
    @staticmethod
    def getXFireworks()->np.ndarray:
        #num fireworks managed by the firework manager...
        numFireworks = len(FireworkManager.fireworks)
        #numParticles per firework
        numParticles = len(FireworkManager.fireworks[0].particlesX)
        #make a np array which will hold X values of all firework particles
        xPositions = np.zeros(numFireworks*numParticles)
        
        #Fill in the xPositions
        for x in range(numFireworks):  #WRONG way to gather all the x position things x.x 

            xValsFirework = FireworkManager.fireworks[x].particlesX

            #starting position of the firework particles
            xSlicePosition =  x*numParticles
            xPositions[xSlicePosition:xSlicePosition+numParticles] = xValsFirework

        return xPositions

    '''
    Returns a numpy array of the y positions of all fireworks particles.
    '''
    @staticmethod
    def getYFireworks()->np.ndarray:
        #num fireworks managed by the firework manager...
        numFireworks = len(FireworkManager.fireworks)
        #numParticles per firework
        numParticles = len(FireworkManager.fireworks[0].particlesY)
        #make a np array which will hold X values of all firework particles
        yParticlePositions = np.zeros(numFireworks*numParticles)
        
        #Fill in the xPositions
        for y in range(numFireworks):
            yValsFirework = FireworkManager.fireworks[y].particlesY
            ySlicePosition =  y*numParticles
            yParticlePositions[ySlicePosition:ySlicePosition+numParticles] = yValsFirework
        return yParticlePositions

    #OH WOW, WE SHOULD JUST HAVE A DRAW FUNCTION DOWN HERE THAT TAKES AX WOW
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
            xFirework = firework.particlesX
            yFirework = firework.particlesY
            FireworkManager.fireworksArtisits[i] = ax.scatter(
                xFirework, yFirework, facecolor=FireworkManager.colors[i])
            i += 1
            print(i)
            print(xFirework)
            


    '''
    Erases the firework artists
    
    '''
    @staticmethod
    def eraseArtists():
        for artist in FireworkManager.fireworksArtisits:
            artist.remove()