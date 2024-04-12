""" 
DIRECTKINEMATIC4 Direct Kinematic.
A04 = DIRECTKINEMATIC4(Q) devuelve la matriz de transformación del
primer sistema de coordenadas al último en función del vector Q 
de variables articulares
 """

import numpy as np
from denavit_hartenberg import denavit_hartenberg

def cinematica_directa(teta, d, a, alfa):

    # Homogeneous transformation matrices between consecutive coordinate systems
    A01 = denavit_hartenberg(teta[0], d[0], a[0], alfa[0])
    A12 = denavit_hartenberg(teta[1], d[1], a[1], alfa[1])
    A23 = denavit_hartenberg(teta[2], d[2], a[2], alfa[2])
    A34 = denavit_hartenberg(teta[3], d[3], a[3], alfa[3])

    # Transformation matrix from the first to the last coordinate system
    A04 = np.dot(np.dot(np.dot(A01, A12), A23), A34)

    # Round the elements of the transformation matrix to 4 decimal places
    A04_rounded = np.round(A04, 4)

    return A04_rounded
