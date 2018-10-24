import numpy as np
a=np.empty((2, 3))
#2 = numero de filas, 3= numero de columnas
for i in range(0,2):
    for j in range(0,3):
        a[i][j] = np.int_([1, 2])

for i in range(0, 2):
    for j in range(0, 3):
        print(a[i][j])
