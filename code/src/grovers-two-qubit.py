from qiskit import *
from qiskit import QuantumCircuit
from qiskit.circuit.quantumcircuit import QuantumCircuit
from qiskit.visualization import plot_histogram



backend = BasicAer.get_backend('qasm_simulator')
#backend = BasicAer.get_backend('statevector_simulator')

#Quantum register
#https://quantumcomputing.stackexchange.com/questions/4907/qiskit-is-there-any-way-to-discard-the-results-of-a-measurement

q = QuantumRegister(2, 'q')
a = QuantumRegister(1, 'a')
c = ClassicalRegister(2, 'c')

#Circuit
circ = QuantumCircuit(q,a,c) # type: qiskit.circuit.quantumcircuit.QuantumCircuit

# ===== prepare the states: psi^{[0]} =====
circ.iden(q[0])
circ.iden(q[1])
circ.x(a[0])

#===== Initialization: psi^{[1]} =====
circ.h(q[0])
circ.h(q[1])
circ.h(a[0])
circ.barrier(q)

#===== Sign flip: psi^{[2]} =====
circ.x(q[0])
circ.ccx(q[0], q[1], a[0])
circ.x(q[0])

circ.barrier(q)

#===== Inversion about average: psi^{[3]} =====
circ.h(q[0])
circ.h(q[1])
circ.x(q[0])
circ.x(q[1])

circ.cz(q[0], q[1])

circ.x(q[0])
circ.x(q[1])
circ.h(q[0])
circ.h(q[1])


#===== Meaurement =====
circ.measure(q,c)

#job
job = execute(circ, backend=backend, shots=1600)
result = job.result()

#circuit
figure = circ.draw(output='mpl')
figure.savefig('../data/images/qiskit-circuit.png')

#histogram
counts = result.get_counts(circ)
print("Total counts:")
print(counts)

figure = plot_histogram(counts)
figure.savefig('../data/images/qiskit-histogram.png')


