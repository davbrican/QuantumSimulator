from Functions import *

n = 1000
qkd = protocol_bb84_simulation(n, mitm=False)

checker = protocol_bb84_checker(qkd, print_results=False)
print(checker)

#print(hex(int("".join([str(bit) for bit in checker["password"]]))))

