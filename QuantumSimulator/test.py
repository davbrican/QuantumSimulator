from Functions import *


n = 1000
qkd = protocol_bb84_simulation(n, mitm=False)

similarity = protocol_bb84_cheker(qkd)
print(similarity)