from qiskit import *
from qiskit import QuantumCircuit
from qiskit.circuit.quantumcircuit import QuantumCircuit
from qiskit.visualization import plot_histogram

backend = BasicAer.get_backend('qasm_simulator')
#backend = BasicAer.get_backend('statevector_simulator')

q = QuantumRegister(2, 'q')
a = QuantumRegister(1, 'a')
c = ClassicalRegister(2, 'c')


circ = QuantumCircuit(q,a,c) # type: qiskit.circuit.quantumcircuit.QuantumCircuit


circ.iden(q[0])
circ.iden(q[1])
circ.x(a[0])
# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(q[0])
circ.h(q[1])
circ.h(a[0])
circ.barrier(q)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
#circ.cx(q[0], q[1])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
# the qubits in a GHZ state.
#circ.cx(q[0], q[2])

circ.x(q[0])
circ.ccx(q[0], q[1], a[0])
circ.x(q[0])

circ.barrier(q)

circ.h(q[0])
circ.h(q[1])
circ.x(q[0])
circ.x(q[1])

circ.cz(q[0], q[1])

circ.x(q[0])
circ.x(q[1])
circ.h(q[0])
circ.h(q[1])


circ.measure(q,c)


#
job = execute(circ, backend=backend, shots=1600)
result = job.result()
#
figura = circ.draw(output='mpl')
figura.savefig('kk2.png')

counts = result.get_counts(circ)
print(counts)

figura = plot_histogram(counts)
figura.savefig('kk.png')

#vector = result.get_statevector(circ)
#print(vector)

