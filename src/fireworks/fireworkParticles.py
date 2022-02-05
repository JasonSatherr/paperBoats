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
        self.particleVelocities = .1*np.random.randn(len(self.particlesX), 2)
        self.timeLived = 0
        self.timeToLive = 12

        #new particles velocity implementation
        xVel , yVel = self.__getInitVelComponents()
        self.particleVelocities = np.block([[xVel],[yVel]])
        self.particleVelocities =.16* self.particleVelocities.transpose()

    '''
    Creates an array or initial speeds for the particles
    '''
    def __getInitSpeed(self):
        speeds = np.random.normal(loc = 1.2, scale = .25, size = len(self.particlesX))
        return speeds

    '''
    creates arrays representing the x and y components of the speed
    '''
    def __getInitSpeedComponents(self):
        speeds = self.__getInitSpeed()
        #take a random chunk of the speed, give it to X
        xSpeed  = np.random.uniform(low = 0, high  = speeds, size = len(speeds))
        #assign the rest to Y
        ySpeedSquared  = np.square(speeds) - np.square(xSpeed)
        ySpeed = np.sqrt(ySpeedSquared)
        
        return xSpeed, ySpeed

    '''
    Gets velocity (directon) of particles
    '''
    def __getInitVelComponents(self):
        xSpeed, ySpeed = self.__getInitSpeedComponents()
        signsX = np.random.choice(a = [-1,1], size = len(xSpeed))  #potential error here :(
        signsY = np.random.choice(a = [-1,1], size = len(ySpeed))  #potential error here :(
        xVel = xSpeed * signsX
        yVel = ySpeed * signsY
        return xVel, yVel

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
    
    

    


