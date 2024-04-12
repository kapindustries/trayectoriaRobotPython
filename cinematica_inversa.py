import numpy as np
from math import atan2
from denavit_hartenberg import denavit_hartenberg

def cinematica_inversa(T, teta, d, a, alfa):
    p = T[0:3, 3]  # Posición de la mano del manipulador
    # Inicialización de las variables articulares a calcular
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    # Solución de la primera articulación: q1
    R = np.sqrt(p[0]**2 + p[1]**2)
    if R**2 - a[1]**2 < 0:
        r = 0
    else:
        r = np.sqrt(R**2 - a[1]**2)
    if R == 0:
        sphi = 0
        cphi = 0
    else:
        sphi = -p[0] / R
        cphi = p[1] / R
    phi = np.arctan2(sphi, cphi)
    if R == 0:
        sbeta = 0
        cbeta = 0
    else:
        sbeta = -a[1] / R
        if r == 0:
            cbeta = 0
        else:
            cbeta = r / R
    beta = np.arctan2(sbeta, cbeta)
    q1 = phi - beta
    # Solución de la segunda articulación: q2
    q2 = p[2] - d[0]
    # Solución de la tercera articulación: q3
    q3 = r - d[3]
    # Solución de la cuarta articulación: q4
    # Cálculo de la matriz de transformación A03
    A01 = denavit_hartenberg(q1, d[0], a[0], alfa[0])
    A12 = denavit_hartenberg(teta[1], q2, a[1], alfa[1])
    A23 = denavit_hartenberg(teta[2], q3, a[2], alfa[2])
    A03 = np.dot(np.dot(A01, A12), A23)
    y3 = A03[0:3, 1]
    sq4 = np.dot(T[0:3, 0], y3)  # Vector orientación n: T(0:3,0)
    cq4 = np.dot(T[0:3, 1], y3)  # Vector orientación s: T(0:3,1)
    q4 = np.arctan2(sq4, cq4)
    # Vector de variables articulares
    q = np.array([q1, q2, q3, q4]).T
    return q
