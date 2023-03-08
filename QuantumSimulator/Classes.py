import numpy
import random
import math

class Qubit:
    
    def __init__(self, alpha = None, beta = None):
        self.alpha = alpha
        self.beta = beta
        if not self.checkState():
            self.generateRandomQubit()
        
    def getState(self):
        return numpy.array([self.alpha, self.beta])
    
    def checkState(self):
        if self.alpha is None or self.beta is None or self.alpha**2 + self.beta**2 != 1:
            return False
        return True
    
    def generateRandomQubit(self):
        self.alpha = random.random()
        self.beta = math.sqrt(1 - self.alpha**2)


    
class Operator:
    
    def __init__(self, gate):
        operator_x = numpy.array([[0, 1], [1, 0]])
        operator_y = numpy.array([[0, -1j], [1j, 0]])
        operator_z = numpy.array([[1, 0], [0, -1]])
        operator_h = numpy.array([[1, 1], [1, -1]]) / numpy.sqrt(2)
        operator_s = numpy.array([[1, 0], [0, 1j]])
        operator_t = numpy.array([[1, 0], [0, numpy.exp(1j * numpy.pi / 4)]])
        operator_cx = numpy.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        operator_cz = numpy.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])
        operator_swap = numpy.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
        operator_toffoli = numpy.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0]])
        
        if gate == 'x':
            self.matrix = operator_x
        elif gate == 'y':
            self.matrix = operator_y
        elif gate == 'z':
            self.matrix = operator_z
        elif gate == 'h':
            self.matrix = operator_h
        elif gate == 's':
            self.matrix = operator_s
        elif gate == 't':
            self.matrix = operator_t
        elif gate == 'cx':
            self.matrix = operator_cx
        elif gate == 'cz':
            self.matrix = operator_cz
        elif gate == 'swap':
            self.matrix = operator_swap
        elif gate == 'toffoli':
            self.matrix = operator_toffoli
        else:
            raise ValueError("Gate not found.")

    def apply(self, qubit):
        return numpy.dot(self.matrix, qubit.getState())
