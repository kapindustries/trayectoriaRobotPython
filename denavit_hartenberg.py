"""
DENAVIT-HARTENBERG Matriz de transformación homogénea.
dh = denavit_hartenberg(TETA, D, A, ALFA) devuelve la matriz de transformacion
homogénea 4 x 4 a partir de los parametros de Denavit-Hartenberg
D, ALFA, A y TETA.
"""

import numpy as np

def denavit_hartenberg(teta, d, a, alfa):
    dh = np.array([[np.cos(teta), -np.cos(alfa)*np.sin(teta), np.sin(alfa)*np.sin(teta), a*np.cos(teta)],
                  [np.sin(teta), np.cos(alfa)*np.cos(teta), -np.sin(alfa)*np.cos(teta), a*np.sin(teta)],
                  [0, np.sin(alfa), np.cos(alfa), d],
                  [0, 0, 0, 1]])
    return dh