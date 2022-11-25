import random
from Qubit import *

class Polarizer:
    
    def __init__(self, angle = None):
        self.angle = angle
        if not self.checkAngle():
            self.angle = random.choice([0, 90])
            
    def __str__(self):
        return f'Polarizer at angle {self.angle}'
    
    def checkAngle(self):
        if self.angle != 0 and self.angle != 90:
            return False
        return True
        
    def polarize(self, qubit):
        if self.angle == 0:
            if random.random() < abs(qubit.alpha)**2:
                qubit.value = 0
            else:
                qubit.value = random.randint(0,1)
        if self.angle == 90:
            if random.random() < abs(qubit.beta)**2:
                qubit.value = 1
            else:
                qubit.value = random.randint(0,1)