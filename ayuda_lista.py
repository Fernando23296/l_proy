'''
a = [0, [435, 757], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(a)-2):
    if (a[i]==[0]):
        a[i]==a[i+1]
print(a)
'''
'''
import numpy

B = numpy.array([])
A = numpy.array([1, 2, 2])
B = numpy.append(B, A)

print (B)
'''
import numpy as np
lista = np.array([[252.  ,0.],
         [435. , 58.],
         [435.,  77.],
         [435., 149.],
         [435., 225.],
         [435., 302.],
         [435., 322.],
         [435., 392.],
         [435., 461.],
         [435., 533.],
         [252., 576.],
         [252., 640.],
         [252., 704.],
         [252., 772.]])
lista= np.delete(lista, 0, 0)
print(lista)
