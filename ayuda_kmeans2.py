from sklearn.cluster import KMeans
import numpy as np
'''
X = np.array([[23,24],
            [54,51],
            [78,75]])
'''
X = np.array([[209, 71],
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
# Number of clusters
k=3
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
