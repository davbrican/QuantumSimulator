import random
from Qubit import *
from Functions import *

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
        if qubit.state == [1,0]:
            if self.angle == qubit.space:
                qubit = Qubit(1,0,self.angle)
                qubit.value = 0
            elif self.angle != qubit.space:
                alpha = random.randint(0,1)
                beta = int(math.sqrt(1 - alpha**2))
                qubit = Qubit(alpha,beta,self.angle)
                qubit = self.polarize(qubit)
        elif qubit.state == [0,1]:
            if self.angle == qubit.space:
                qubit = Qubit(0,1,self.angle)
                qubit.value = 1
            elif self.angle != qubit.space:
                alpha = random.randint(0,1)
                beta = int(math.sqrt(1 - alpha**2))
                qubit = Qubit(alpha,beta,self.angle)
                qubit = self.polarize(qubit)
        else:
            if self.angle == 0:
                if random.random() < abs(qubit.alpha)**2:
                    qubit.value = 0
                else:
                    qubit.value = random.randint(0,1)
            elif self.angle == 90:
                if random.random() < abs(qubit.beta)**2:
                    qubit.value = 1
                else:
                    qubit.value = random.randint(0,1)
                qubit.generateQubitFromBit(qubit.value, self)

        return qubit