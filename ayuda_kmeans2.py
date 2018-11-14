from sklearn.cluster import KMeans
import numpy as np
'''
X = np.array([[23,24],
            [54,51],
            [78,75]])
'''
X = np.array([[168, 907],
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
# Number of clusters
k=2
kmeans = KMeans(k)
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_
# Comparing with scikit-learn centroids
#print(C)  # From Scratch
print(centroids)  # From sci-kit learn
print("*"*20)
for i in range(0,k):
    print("*"*10)
    print(centroids[i])
