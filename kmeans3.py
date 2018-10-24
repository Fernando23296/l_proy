import numpy as np
from spicy.spatial import distance_matrix
import matplotlib.pyplot as plt


def k_means(X, K):
	nrow = X.shape[0]
	ncol = X.shape[1]

	initial_centroids = np.random.choice(now, K, replace=False)

	centroids = X[initial_centroids]
	centroids_old = np.zeros((K, ncol))

	cluster_assigments = np.zeros(nrow)
	while(centroids_old != centroids).any():
		centroids_old = centroids.copy()

		dist_matrix = distance_matrix(X, centroids, p=2)
		for i in np.arange(nrow):
			d = dist_matrix[i]
			closest_centroid = (np.where(d == np.min(d)))[0][0]
			cluster_assigments[i] = closest_centroid

		for k in np.arange(K):
			Xk = X[cluster_assigments == k]
			centroids[k] = np.apply_along_axis(np.mean, axis=0, arr=Xk)
	return (centroids, cluster_assigments)


x_cluster_1 = np.arange(2, 6, 0.2)
y_cluster_1 = 1 + (np.random.normal(0, 1, len(x_cluster_1)))*2

x_cluster_2 = np.arange(14, 18, 0.2)
y_cluster_2 = 1 + (np.random.normal(0, 1, len(x_cluster_2)))*2

x_cluster_3 = np.arange(7, 12, 0.2)
y_cluster_3 = 1 + (np.random.normal(0, 1, len(x_cluster_3)))*2

data = np.column_stack((x, y))

K = 3
k_means_result = k_means(data, K)

centroids = k_means_result[0]
cluster_assigments = (k_means_result[1]).tolist()

colors = ['r', 'g', 'b']


def f(x): return colors[int(x)]


cluster_assigments = list(map(f, cluster_assigments))

my_dpi = 96
plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Clustering\n')

plt.scatter(data[:, 0], data[:, 1], color=cluster_assigments, s=20)
plt.savefig('k_means.png')
