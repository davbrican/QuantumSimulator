#  1. QuantumSimulator

This is a project to simulate Quantum Cryptography Protocols.

This project is a simplified simulation of qubits and polarizers, so it just work on a bidimensional space, what means that Qubits value will be always between [0,1] and the calculations will not take into account the complex part.

There is a BB84 transference protocol simulation to study the Qubits behaviours.

There are 2 classes and some functions to emulate the Quantum behaviour.

## 1.1. Classes
### 1.1.1. Qubit()
A Qubit can be created by default with a random state, or with specific data.
You can call the class instance *Qubit()* to create a random Qubit, or introducing a valid state inside de constructor:

`example_qubit = Qubit(alpha, beta)`

Where:

∣α∣²+∣β∣²=1

Another way to generate a new qubit, is creating it from a regular bit using:

`example_qubit = generateQubitFromBit(bit, polarizer)`

Where *bit* must be equal **0** or **1** and *polarizer* must be an existing polarizer

### 1.1.2. Polarizer()
A Polarizer can be also created by default as a random polarizer (what means that its angle will be random 0 or 90), and can also be created by its constructor specifying the angle used (remember that this value must be 0 or 90):


`example_polarizer = Polarizer()`

*or*

`example_polarizer = Polarizer(angle)`
Where *angle* must be equal **0** or **90**


A useful and neccesary function in class *Polarizer()* is *.polarize()* used to measure a Qubit, e.g.:

`qubit = Qubit()`

`polarizer = Polarizer()`

`polarizer.polarize(qubit)`

## Functions
### createNQubits(n)
Returns a list of random Qubits given *n* (integer number > 0)
### createNPolarizers(n)
Returns a list of random Polarizers given *n* (integer number > 0)
### createNBits(n)
Returns a list of random Bits [0,1] given *n* (integer number > 0)
### createNQubitsFromBits(bits, polarizers)
Returns a list of Qubits given a list of *bits* and a list of *polarizers*
### polarizeQubits(qubits,  polarizers)
Returns a list of measured *qubits* given a list of qubits and another of *polarizers*
### duplicateQubit(qubit)
Returns a copy of a bit given a *qubit* (This function is really useful because after measure a Qubit, it completely changes and lose its original state, so in case that you need have a copy to study results, you must previously create a copy of the qubit)
### protocol_bb84_simulation(n, mitm)
Generate a full QKD protocol simulation and returns an object with the attributes:
 - *a_bits* (original bits generated)
 - *a_polarizers* ("Alice" Sender polarizers)
 - *a_qubits* ("Alice" Sender generated Qubits from the original bits)
 - *b_polarizers* ("Bob" Receiver polarizers)
 - *b_bits* ("Alice" Receiver generated Qubits after polarize "Alice" Sender qubits)
### protocol_bb84_cheker(qkd)
Returns a percentage of similarity in qkd protocol (100% if there is not MiTM attack)