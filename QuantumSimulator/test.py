from Functions import *

a_qubits = createNQubits(8)
a_polars = createNPolarizers(8)
a_qubits_copy = [duplicateQubit(qubit) for qubit in a_qubits]
a_polarized_qbits = polarizeQubits(a_qubits_copy, a_polars)

b_qubits = createNQubitsFromBits([bit.value for bit in a_polarized_qbits])
b_polars = createNPolarizers(8)
b_qubits_copy = [duplicateQubit(qubit) for qubit in b_qubits]
b_polarized_qbits = polarizeQubits(b_qubits_copy, b_polars)


for i in range(8):    
    print(a_qubits[i])
    print(a_polars[i])
    print(a_polarized_qbits[i].value)
    
    print(b_qubits[i])
    print(b_polars[i])
    print(b_polarized_qbits[i].value)
    
    print("")