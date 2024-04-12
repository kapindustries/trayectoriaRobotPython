from planifica import planifica
from animacion import animacion
import numpy as np
from cinematica_inversa import cinematica_inversa
from cinematica_directa import cinematica_directa
from dibujar_robot_3d import dibujar_robot_3d

# LETRA U
p1=[0.4, 0.4, 0.45]
p2=[0.3, 0.4, 0.45]
p3=[0.3, 0.3, 0.45]
p4=[0.4, 0.3, 0.45]

# LETRA A
p5=[0.2, 0.3, 0.35]
p6=[0.3, 0.3, 0.35]
p7=[0.3, 0.2, 0.35]
p8=[0.25, 0.2, 0.35]
p9=[0.25, 0.3, 0.35]
p10=[0.25, 0.2, 0.35]
p11=[0.2, 0.2, 0.35]

# LETRA O
p12=[0.2, 0.2, 0.25]
p13=[0.1, 0.2, 0.25]
p14=[0.1, 0.1, 0.25]
p15=[0.2, 0.1, 0.25]
p16=[0.2, 0.2, 0.25]



n=[1, 0, 0]
s=[0, 1, 0]
a=[0, 0, 1]
npuntos=50

q1 = np.deg2rad(0)  # Articulación rotacional
q2 = 0   # Articulación prismática
q3 = 0    # Articulación prismática
q4 = np.deg2rad(0)    # Articulación rotacional

teta = np.array([q1, 0, 0, q4])
d = np.array([0.4, q2, q3, 0.2])
al = np.array([0, -0.1, 0, 0])
alfa = np.array([0, -np.pi/2, 0, 0])

#dibujar_robot_3d(teta, d, al, alfa)
A04 = cinematica_directa(teta, d, al, alfa)
mat_q_1 =planifica(p1, p2, n, s, a, npuntos,teta,d,al,alfa)
mat_q_2 =planifica(p2, p3, n, s, a, npuntos,teta,d,al,alfa)
mat_q_3 =planifica(p3, p4, n, s, a, npuntos,teta,d,al,alfa)
mat_q_5 =planifica(p5, p6, n, s, a, npuntos,teta,d,al,alfa)
mat_q_6 =planifica(p6, p7, n, s, a, npuntos,teta,d,al,alfa)
mat_q_7 =planifica(p7, p8, n, s, a, npuntos,teta,d,al,alfa)
mat_q_8 =planifica(p8, p9, n, s, a, npuntos,teta,d,al,alfa)
mat_q_9 =planifica(p9, p10, n, s, a, npuntos,teta,d,al,alfa)
mat_q_10 =planifica(p10, p11, n, s, a, npuntos,teta,d,al,alfa)
mat_q_12 =planifica(p12, p13, n, s, a, npuntos,teta,d,al,alfa)
mat_q_13 =planifica(p13, p14, n, s, a, npuntos,teta,d,al,alfa)
mat_q_14 =planifica(p14, p15, n, s, a, npuntos,teta,d,al,alfa)
mat_q_15 =planifica(p15, p16, n, s, a, npuntos,teta,d,al,alfa)

l = np.hstack((mat_q_1, mat_q_2, mat_q_3,mat_q_5, mat_q_6,mat_q_7, mat_q_8,mat_q_9, mat_q_10, mat_q_12,mat_q_13, mat_q_14,mat_q_15))
animacion(l,teta,d,al,alfa)

