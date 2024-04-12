import numpy as np
from cinematica_inversa import cinematica_inversa

# Matriz de transformación que representa la posición y orientación de la mano del manipulador

T = np.array([[ 0.5403, -0,     -0.8415, -0.2223],
 [ 0.8415,  0,      0.5403,  0.0239],
 [ 0,     -1,      0,      0.4   ],
 [ 0,      0,      0,      1,    ]])

q=[0,0,0,0]
teta = np.array([q[0], 0, 0, q[3]])
d = np.array([0.4, q[1], q[2], 0.2])
a = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])

# Calcular el vector de coordenadas articulares correspondiente a la solución cinemática inversa
q = cinematica_inversa(T,teta,d,a,alfa)

q_rounded = np.round(q, 4)

# Imprimir el vector de coordenadas articulares
print(q_rounded)
