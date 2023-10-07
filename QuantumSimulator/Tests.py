from Functions import *
from Qubit import *
from Polarizer import *

'''
n = 1000
qkd = protocol_bb84_simulation(n, mitm=True)

checker = protocol_bb84_checker(qkd, print_results=False)
print(checker)

#print(hex(int("".join([str(bit) for bit in checker["password"]]))))

print(hex(int("".join([str(bit) for bit in checker["password"]]))))
print(bin(int("".join([str(bit) for bit in checker["password"]]))))

qubit1 = Qubit(1, 0, 0)
qubit2 = Qubit(0, 1, 0)
qubit3 = Qubit(0.6, 0.8, 90)

qubit1.quantumEntangle(qubit2)
qubit2.quantumEntangle(qubit3)

print(qubit1)
print(qubit2)
print(qubit3)

print("")
Polarizer(0).polarize(qubit1)
print("")

print(qubit1)
print(qubit2)
print(qubit3)

'''
print(coin_flipping("A"))