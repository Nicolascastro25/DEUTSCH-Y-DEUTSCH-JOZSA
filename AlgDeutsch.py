import numpy as np
# Import Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as mpl

#El Aerproveedor contiene una variedad de backends de simuladores de alto rendimiento para una variedad de métodos de simulación.
#Se crea un nuevo backend de simulador
slt = Aer.get_backend('qasm_simulator')

print("Funcion 1")
print("0--->0")
print("1--->0")
#Crear un nuevo circuito.
c = QuantumCircuit(2, 1)
#Aplicar la puerta base X.
c.x(1)
#La barrera actúa como una directiva para la compilación de circuitos para separar partes de un circuito
c.barrier()
#Aplicar compuerta de Hadamard de un solo qubit.
c.h(0)
#Aplicar compuerta de Hadamard de un solo qubit.
c.h(1)
#La barrera actúa como una directiva para la compilación de circuitos para separar partes de un circuito
c.barrier()
#La barrera actúa como una directiva para la compilación de circuitos para separar partes de un circuito
c.barrier()
#Aplicar compuerta de Hadamard de un solo qubit.
c.h(0)
#La barrera actúa como una directiva para la compilación de circuitos para separar partes de un circuito
c.barrier()
# Medimos bits cuánticos en bits clásicos (tuplas).
c.measure([0],[0])
#La barrera actúa como una directiva para la compilación de circuitos para separar partes de un circuito
c.barrier()
#Transpila uno o más circuitos, de acuerdo con algunos objetivos dados
comC = transpile(c, slt)
#Devuelve el trabajo de la simulación
trabajo = slt.run(comC, shots=1000)
#Obtener resultado del trabajo.
r = trabajo.result()
#Obtener los datos del histograma de un experimento.
recorrido = r.get_counts(c)
#Imprime los datos obtenidos del histograma
print("\nEl recuento total para 0 y 1 es:",recorrido)
#imprimimos el circuito
print(c)
#Trazar un histograma de datos de recuentos de entrada.
plot_histogram(recorrido)
#Mostrar todas las figuras abiertas.
mpl.show()


#Para cada una de las siguientes lineas no se documentará puesto que la definición de las funciones son las usadas en el apartado anterior.
print("Funcion 2")
print("0--->0")
print("1--->1")
c = QuantumCircuit(2, 1)
c.x(1)
c.barrier()
c.h(0)
c.h(1)
c.barrier()
c.cnot(0,1)
c.barrier()
c.h(0)
c.barrier()
c.measure([0],[0])
c.barrier()
comC = transpile(c, slt)
trabajo = slt.run(comC, shots=1000)
r = trabajo.result()
recorrido = r.get_counts(c)
print("\nEl recuento total para 0 y 1 es:",recorrido)
print(c)
plot_histogram(recorrido)
mpl.show()

print("Funcion 3")
print("0--->1")
print("1--->0")
c = QuantumCircuit(2, 1)
c.x(1)
c.barrier()
c.h(0)
c.h(1)
c.barrier()
c.x(0)
c.cnot(0,1)
c.x(0)
c.barrier()
c.h(0)
c.barrier()
c.measure([0],[0])
c.barrier()
comC = transpile(c, slt)
trabajo = slt.run(comC, shots=1000)
r = trabajo.result()
recorrido = r.get_counts(c)
print("\nEl recuento total para 0 y 1 es:",recorrido)
print(c)
plot_histogram(recorrido)
mpl.show()

print("Funcion 4")
print("0--->1")
print("1--->1")
c = QuantumCircuit(2, 1)
c.x(1)
c.barrier()
c.h(0)
c.h(1)
c.barrier()
c.x(1)
c.barrier()
c.h(0)
c.barrier()
c.measure([0],[0])
c.barrier()
comC = transpile(c, slt)
trabajo = slt.run(comC, shots=1000)
r = trabajo.result()
recorrido = r.get_counts(c)
print("\nEl recuento total para 0 y 1 es:",recorrido)
print(c)
plot_histogram(recorrido)
mpl.show()