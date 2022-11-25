from Polarizer import *
from Qubit import *
import random

def createNQubits(n):
    return [Qubit() for i in range(n)]

def createNPolarizers(n):
    return [Polarizer() for i in range(n)]

def createNBits(n):
    return [random.randint(0,1) for i in range(n)]

def createNQubitsFromBits(bits):
    return [Qubit().generateFromBit(bit) for bit in bits]

def polarizeQubits(qubits, polarizers):
    for i in range(len(qubits)):
        polarizers[i].polarize(qubits[i])
    return qubits

def duplicateQubit(qubit):
    return Qubit(qubit.alpha, qubit.beta)