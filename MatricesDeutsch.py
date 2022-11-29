import numpy as np
# Import Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as mpl

def traducirbits(n):
    aux = 0
    r = 0
    while aux < len(n):
        r += int(n[-1-aux])*(2**aux)
        aux += 1
    return r
    
def imprimir(m):
    for i in m:
        print(" ".join(list(map(str,i))))
        
#El Aerproveedor contiene una variedad de backends de simuladores de alto rendimiento para una variedad de métodos de simulación.
#Se crea un nuevo backend de simulador
slt = Aer.get_backend('qasm_simulator')

print("Funcion 1")
print("0--->0")
print("1--->0")
a1 = [[0 for k in range(4)] for l in range(4)]
aux = 0
for i in range(2):
    for j in range(2):
        #Crear un nuevo circuito.
        c = QuantumCircuit(2, 2)
        if i == 1:
            #Aplicar la puerta base X.
            c.x(0)
        if j == 1:
            #Aplicar la puerta base X.
            c.x(1)
        #La barrera actúa como una directiva para la compilación de circuitos para separar partes de un circuito
        c.barrier()
        #La barrera actúa como una directiva para la compilación de circuitos para separar partes de un circuito
        c.barrier()
        # Medimos bits cuánticos en bits clásicos (tuplas).
        c.measure([0,1],[1,0])
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
        for k in recorrido:
            a1[traducirbits(k)][aux] = 1
        aux += 1
imprimir(a1)

#Para cada una de las siguientes lineas no se documentará puesto que la definición de las funciones son las usadas en el apartado anterior.

print("Funcion 2")
print("0--->0")
print("1--->1")
a2 = [[0 for k in range(4)] for l in range(4)]
aux = 0
for i in range(2):
    for j in range(2):
        c = QuantumCircuit(2, 2)
        if i == 1:
            c.x(0)
        if j == 1:
            c.x(1)
        c.barrier()
        c.cnot(0,1)
        c.barrier()
        c.measure([0,1],[1,0])
        c.barrier()
        comC = transpile(c, slt)
        trabajo = slt.run(comC, shots=1000)
        r = trabajo.result()
        recorrido = r.get_counts(c)
        for k in recorrido:
            a2[traducirbits(k)][aux] = 1
        aux += 1
imprimir(a2)

print("Funcion 3")
print("0--->1")
print("1--->0")
a3 = [[0 for k in range(4)] for l in range(4)]
aux = 0
for i in range(2):
    for j in range(2):
        c = QuantumCircuit(2, 2)
        if i == 1:
            c.x(0)
        if j == 1:
            c.x(1)
        c.barrier()
        c.x(0)
        c.cnot(0,1)
        c.x(0)
        c.barrier()
        c.measure([0,1],[1,0])
        c.barrier()
        comC = transpile(c, slt)
        trabajo = slt.run(comC, shots=1000)
        r = trabajo.result()
        recorrido = r.get_counts(c)
        for k in recorrido:
            a3[traducirbits(k)][aux] = 1
        aux += 1
imprimir(a3)

print("Funcion 4")
print("0--->1")
print("1--->1")
a4 = [[0 for k in range(4)] for l in range(4)]
aux = 0
for i in range(2):
    for j in range(2):
        c = QuantumCircuit(2, 2)
        if i == 1:
            c.x(0)
        if j == 1:
            c.x(1)
        c.barrier()
        c.x(1)
        c.barrier()
        c.measure([0,1],[1,0])
        c.barrier()
        comC = transpile(c, slt)
        trabajo = slt.run(comC, shots=1000)
        r = trabajo.result()
        recorrido = r.get_counts(c)
        for k in recorrido:
            a4[traducirbits(k)][aux] = 1
        aux += 1
imprimir(a4)