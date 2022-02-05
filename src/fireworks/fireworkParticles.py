from msilib.schema import Class

import numpy as np

'''
Class that manages positions and velocity of fireworks

Implement acceleration later (negative acc)
'''
class FireworkParticles:

    def __init__(self, xSpawnPoint, ySpawnPoint) -> None:
        #The xPosition of the fireworks particles
        self.particlesX = np.ndarray(64)
        self.particlesX[:] = xSpawnPoint
        #The yPosition of the particles
        self.particlesY = np.ndarray(len(self.particlesX))
        self.particlesY[:] = ySpawnPoint

        #The rand normal velocities of each particle
        self.particleVelocities = .08*np.random.randn(len(self.particlesX), 2)
        self.timeLived = 0
        self.timeToLive = 10

    '''
    Updates the positions of the firework's particles
    '''
    def update(self):

        if (not self.isDead()): #it's alive
            #adjust the positions
            self.updateX()
            self.updateY()
            #increate the time lived
            self.timeLived += 1
        else:
            self.hideParticles()

    def isDead(self):
        return self.timeLived >= self.timeToLive


    def hideParticles(self):
        self.particlesX = np.empty(len(self.particlesX))
        self.particlesX.fill(-5)
        self.particlesY = np.empty(len(self.particlesY))
        self.particlesY.fill(-5)
    '''Updates the x positions of the firework's particles'''
    def updateX(self):
        #slow down the particles due to air resistance
        self.particleVelocities[:, 0] = .94 * self.particleVelocities[:, 0]
        self.particlesX = self.particleVelocities[:, 0] + self.particlesX[:]

    '''Updates the y positions of the firework's particles'''
    def updateY(self):
        #simulate an acceleration downwards...
        self.particleVelocities[:, 1] = self.particleVelocities[:, 1] - .009
        #slow down to account of air resistance
        self.particleVelocities[:, 1] = .95* self.particleVelocities[:, 1]
        self.particlesY = self.particleVelocities[:, 1] + self.particlesY[:]
    
    

    


