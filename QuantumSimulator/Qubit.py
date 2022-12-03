import random
import math
from Polarizer import *
from Functions import *

class Qubit:
    
    def __init__(self, alpha = None, beta = None, space = None):
        self.alpha = alpha
        self.beta = beta
        self.space = space
        if not self.checkState():
            self.generateRandomQubit()
        self.value = None
        self.entanglements = []
        
    def __str__(self):
        return f'Qubit state: {self.getState()} in space {self.space}' if self.value is None else f'Qubit value: {self.value}'
        
    def getState(self):
        return [self.alpha, self.beta]
    
    def checkState(self):
        if self.alpha is None or self.beta is None or self.alpha**2 + self.beta**2 != 1:
            return False
        if self.space != 0 and self.space != 90:
            return False
        return True
    
    def generateRandomQubit(self):
        self.alpha = random.random()
        self.beta = math.sqrt(1 - self.alpha**2)
        self.space = random.choice([0, 90])
        
    def generateQubitFromBit(self, bit, polarizer):
        if bit == 0:
            return Qubit(1, 0, polarizer.angle)
        elif bit == 1:
            return Qubit(0, 1, polarizer.angle)
        
    def quantumEntangle(self, qubit):
        if qubit not in self.entanglements:
            self.entanglements.append(qubit)
            qubit.quantumEntangle(self)

    def quantumEntanglement(self):
        for i in self.entanglements:
            if (i.alpha != self.alpha or i.beta != self.beta or i.space != self.space):
                i.alpha, i.beta, i.space, i.value = self.alpha, self.beta, self.space, self.value
                i.quantumEntanglement()