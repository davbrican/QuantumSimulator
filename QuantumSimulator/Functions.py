from Polarizer import *
from Qubit import *
import random

def createNQubits(n):
    return [Qubit() for i in range(n)]

def createNPolarizers(n):
    return [Polarizer() for i in range(n)]

def createNBits(n):
    return [random.randint(0,1) for i in range(n)]

def createNQubitsFromBits(bits, polarizers):
    return [Qubit().generateQubitFromBit(bits[i], polarizers[i]) for i in range(len(bits))]

def polarizeQubits(qubits, polarizers):
    for i in range(len(qubits)):
        qubits[i] = polarizers[i].polarize(qubits[i])
    return qubits

def duplicateQubit(qubit):
    return Qubit(qubit.alpha, qubit.beta, qubit.space)

def protocol_bb84_simulation(n, mitm=False):
    a_bits = createNBits(n)
    a_polarizers = createNPolarizers(n)
    a_qubits = createNQubitsFromBits(a_bits, a_polarizers)
    qubits_copy = [duplicateQubit(qubit) for qubit in a_qubits]
    
    b_polarizers = createNPolarizers(n)
        
    if mitm:
        mitm_polarizers = createNPolarizers(n)
        mitm_bits = polarizeQubits(qubits_copy, mitm_polarizers)
        b_bits = polarizeQubits(mitm_bits, b_polarizers)
    else:
        b_bits = polarizeQubits(qubits_copy, b_polarizers)
    
    return {"a_bits": a_bits, "a_polarizers": a_polarizers, "a_qubits": a_qubits, "b_polarizers": b_polarizers, "b_bits": b_bits}

def protocol_bb84_checker(qkd, print_results=False):
    n = len(qkd["a_qubits"])
    random_start = random.randint(0, n-int(n/4))
    random_end = int(random_start + (n/4))

    a_comparison_bits = [bit for bit in qkd["a_bits"][random_start:random_end]]
    a_comparison_polars = [qbit.angle for qbit in qkd["a_polarizers"][random_start:random_end]]
    b_comparison_bits = [qbit.value for qbit in qkd["b_bits"][random_start:random_end]]
    b_comparison_polars = [qbit.angle for qbit in qkd["b_polarizers"][random_start:random_end]]
    
    del qkd["a_bits"][random_start:random_end]
    del qkd["a_polarizers"][random_start:random_end]
    del qkd["a_qubits"][random_start:random_end]
    del qkd["b_bits"][random_start:random_end]
    del qkd["b_polarizers"][random_start:random_end]
    
    total_equal = 0
    total_equally_polarized = 0
    for i in range(int(n/4)):
        if a_comparison_polars[i] == b_comparison_polars[i]:
            total_equally_polarized += 1
            if a_comparison_bits[i] == b_comparison_bits[i]:
                total_equal += 1
            elif print_results:
                print(f"Bits are not equal at index {i}: a_bit={a_comparison_bits[i]}, b_bit={b_comparison_bits[i]} at angles: a {a_comparison_polars[i]} b {b_comparison_polars[i]}")
    equallity_percentage = total_equal/total_equally_polarized*100 if total_equally_polarized != 0 else 0
    password = [qbit.value for qbit in qkd["b_bits"]]  if equallity_percentage == 100 else []

    return {"equallity_percentage": equallity_percentage, "password": password}