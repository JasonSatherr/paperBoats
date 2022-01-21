from msilib.schema import Class

import numpy as np

'''
Class that manages positions and velocity of fireworks
'''
class FireworkParticles:

    def __init__(self, xSpawnPoint, ySpawnPoint) -> None:
        #The xPosition of the fireworks particles
        self.particlesX = np.ndarray(8)
        self.particlesX[:] = xSpawnPoint
        #The yPosition of the particles
        self.particlesY = np.ndarray(len(self.particlesX))
        self.particlesY[:] = ySpawnPoint

        #The rand normal velocities of each particle
        self.particleVelocities = .08*np.random.randn(len(self.particlesX), 2)

    def update(self):
        self.updateX()
        self.updateY()

    def updateX(self):
        self.particlesX = self.particlesX[:] + self.particleVelocities[:, 0]

    def updateY(self):
        self.particlesY = self.particlesY[:] + self.particleVelocities[:, 1]
    
    

    


