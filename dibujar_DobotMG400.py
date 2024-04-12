""" 
dibujar_DobotMG400.
Este arhivo de ejemplo crea la visualizacion del robot Dobot MG400
usando la funcion dibujar_robot_3d() los valores articulares son 
 """

import numpy as np
from dibujar_robot_3d import dibujar_robot_3d


# Valores de los parámetros D-H
q1 = np.deg2rad(0)  # Articulación rotacional
q2 = np.deg2rad(33)    # Articulación prismática
q3 = np.deg2rad(-33)    # Articulación prismática
q4 = np.deg2rad(-40)    # Articulación rotacional

teta = np.array([q1, q2, q3, q4])
d = np.array([115, 0, 0, 0])
a = np.array([0, 175, 175, 66])
alfa = np.array([np.pi/2, 0, 0, np.pi/2])

dibujar_robot_3d(teta, d, a, alfa)