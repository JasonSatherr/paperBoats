import numpy as np
from fireworks.fireworkParticles import FireworkParticles


class FireworkManager:
    fireworks = np.array( [FireworkParticles(0,0) for i in range(10)],
                    dtype=object)

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
    @param yVal The y position for the firewor
    '''
    @staticmethod
    def spawnFirework(n, xVal, yVal):
        FireworkManager.fireworks[n] = FireworkParticles(xVal,yVal)

    '''
    Returns a numpy array of the x positions of all fireworks particles.
    '''
    @staticmethod
    def getXFireworks():
        xPositions = np.ndarray(len(FireworkManager.fireworks)*len(fire))
