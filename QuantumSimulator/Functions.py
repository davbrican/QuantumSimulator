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

def protocol_bb84_simulation(n, mitm=False, printResults=False):
    a_qubits = createNQubits(n)
    a_polars = createNPolarizers(n)
    a_qubits_copy = [duplicateQubit(qubit) for qubit in a_qubits]
    a_polarized_qbits = polarizeQubits(a_qubits_copy, a_polars)

    if mitm:
        mitm_qubits = createNQubitsFromBits([bit.value for bit in a_polarized_qbits])
        mitm_polars = createNPolarizers(n)
        mitm_qubits_copy = [duplicateQubit(qubit) for qubit in mitm_qubits]
        mitm_polarized_qbits = polarizeQubits(mitm_qubits_copy, mitm_polars)

        b_qubits = createNQubitsFromBits([bit.value for bit in mitm_polarized_qbits])
    else:
        b_qubits = createNQubitsFromBits([bit.value for bit in a_polarized_qbits])
    b_polars = createNPolarizers(n)
    b_qubits_copy = [duplicateQubit(qubit) for qubit in b_qubits]
    b_polarized_qbits = polarizeQubits(b_qubits_copy, b_polars)

    return {"a_qubits": a_qubits, "a_polars": a_polars, "a_polarized_qbits": a_polarized_qbits, "b_qubits": b_qubits, "b_polars": b_polars, "b_polarized_qbits": b_polarized_qbits}

def protocol_bb84_cheker():
    return True