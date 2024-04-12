import numpy as np
from cinematica_directa import cinematica_directa

# Ejemplo de uso

q=[1,0,0,0]
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])

A04 = cinematica_directa(teta, d, a, alfa)

# Imprimir la matriz de transformación homogénea
print(A04)