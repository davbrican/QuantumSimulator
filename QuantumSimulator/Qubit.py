import random
import math
from Polarizer import *

class Qubit:
    
    def __init__(self, alpha = None, beta = None):
        self.alpha = alpha
        self.beta = beta
        self.state = [self.alpha, self.beta]
        if not self.checkState():
            self.generateRandomQubit()
        self.value = None
        
    def __str__(self):
        return f'Qubit state: {self.state}' if self.value is None else f'Qubit value: {self.value}'
        
    def checkState(self):
        if self.alpha is None or self.beta is None or self.alpha**2 + self.beta**2 != 1:
            return False
        return True
    
    def generateRandomQubit(self):
        self.alpha = random.random()
        self.beta = math.sqrt(1 - self.alpha**2)
        self.state = [self.alpha, self.beta]
        
    def generateFromBit(self, bit):
        if bit == 0:
            self.alpha = 1
            self.beta = 0
        elif bit == 1:
            self.alpha = 0
            self.beta = 1
        self.state = [self.alpha, self.beta]
        return self