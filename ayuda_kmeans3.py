'''
GRAFICA LOS PUNTOS
'''
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

#x1 = np.array([209,214,263,187,243,198,209,186,191,245,189,187,177,264,174,247,229])
#x2 = np.array([71, 64, 60, 55, 49, 42, 41, 39,39, 34, 30, 24, 10, 10, 8, 1, 1])
#x1 = np.array([209, 214, 263, 187, 243, 198, 209, 186,191, 245, 189, 187, 177, 264, 174, 247, 229])
'''
xpro = np.array([[209, 71],
                     [214, 64],
                     [263, 60],
                     [187, 55],
                     [243, 49],
                     [198, 42],
                     [209, 41],
                     [186, 39],
                     [191, 39],
                     [245, 34],
                     [189, 30],
                     [187, 24],
                     [177, 20],
                     [264, 10],
                     [174, 8],
                     [247, 1],
                     [229, 1]])
                    
'''
xpro = np.array([[168, 907], 
[184, 903], 
[384, 893], 
[299, 878], 
[247, 875], 
[390, 865], 
[216, 862], 
[168, 880], 
[180, 877], 
[300, 845], 
[175, 843], 
[169, 845]])
tam=len(xpro)
x1 = np.empty([tam])
for i in range(0,tam):
    x1[i] = int(xpro[i][0])
x2 = np.empty([tam])
for i in range(0, tam):
    x2[i] = int(xpro[i][1])

plt.plot()
plt.xlim([0, 400])
plt.ylim([800, 1000])
plt.title('Seleccion K-means, K=2')
plt.scatter(x1, x2)
plt.show()

# create new plot and data
plt.plot()
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']

K = 2
kmeans_model = KMeans(n_clusters=K).fit(X)

plt.plot()
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l], ls='None')
    plt.xlim([0, 400])
    plt.ylim([800, 1000])

plt.plot(343.25, 870.25, marker='o', markersize=3, color="black")
plt.plot(188.375, 874, marker='o', markersize=3, color="black")
plt.show()

