from sklearn.cluster import KMeans
import numpy as np
from random import *

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

lista=[
    [[200, 74], [349, 68], [378, 69], [254, 59], [248, 57], 
    [236, 56], [241, 53], [205, 52], [197, 49], [232, 46], 
    [314, 46], [322, 42], [265, 31], [320, 25], [246, 15], 
    [268, 13], [212, 3], [263, 1]], 

    [[209, 147], [311, 145], [258, 147], [215, 132], [224, 129], 
    [383, 130], [339, 127], [325, 126], [201, 125], [363, 122], 
    [202, 120], [293, 118], [277, 119], [243, 112], [313, 106], 
    [374, 103], [353, 96], [365, 95], [314, 87], [310, 80], 
    [304, 80], [221, 80]], 
    
    [[302, 224], [278, 221], [356, 220], [205, 222], [341, 202],
    [366, 201], [342, 196], [216, 195], [363, 195], [251, 193], 
    [289, 187], [353, 188], [314, 185], [236, 186], [303, 182], 
    [280, 182], [255, 182], [352, 177], [211, 174], [351, 171], 
    [388, 168], [223, 166], [301, 163], [210, 164], [288, 159], 
    [220, 157]], 
    
    [[209, 299], [214, 292], [263, 288], [187, 283], [243, 277], 
    [198, 270], [209, 269], [186, 267], [191, 267], [245, 262], 
    [189, 258], [187, 252], [177, 248], [264,238], [174, 236], 
    [247, 229],[229, 229]], 
    
    [[241, 378], [259, 352], [260, 336], [244, 328], [258, 324],
    [255, 316], [254, 306]], 
    
    [[254, 450], [303, 447], [327, 441], [352, 431], [249, 432], 
    [245, 400], [297,396], [278, 391], [294, 389], [289, 382]], 
    
    [[239, 528], [294, 520], [268, 517], [247, 513], [290, 512],
    [285, 492], [267, 492], [276, 486], [269, 479], [231, 481], 
    [266, 469], [286, 468], [225, 468], [240, 466], [229, 457]], 
    
    [[229, 595], [226, 585], [280, 574], [226, 569], [282, 536], 
    [237, 532]], 
    
    [[278, 682],[237, 675], [291, 671], [242, 651], [270, 642],
     [268, 637], [247, 630], [284, 617], [314, 615], [259, 615], 
     [271, 614]], 
     
    [[263, 750], [325, 742], [266, 741], [290, 729], [275, 718], 
    [338, 703], [292, 698], [335, 694], [276, 693], [357, 693], 
    [333, 689], [290, 690]], 
    
    [[283, 830]], 
    
    [[280, 891], [338, 883], [277, 884]]]


lis2=[[[340, 87]], [[340, 174]], [[340, 261]], [[440, 351], [383, 359], [326, 364]], [[326, 520], [383, 516], [440, 508], [493, 487], [540, 440]], [[540, 597],
                                                                                                                                                [564, 549]], [[564, 669], [556, 621]], [[556, 778], [540, 739], [517, 699]], [[517, 856], [470, 809]], [[417, 935], [366, 899], [318, 875]], [[318, 1032]]]
def contador(l):
    tam=len(l)
    for i in range(0,tam):
        tam1=len(l[i])
        #for ii in range(0,tam1):
        print("*"*40)
        print(tam1)


def seleccionador(l):
    a = []
    tam = len(l)
    for i in range(1, tam):
        tam1 = (len(l[i])-1)

        a.append(l[i][randint(0, tam1)])
    return a

def contador(l):
    tam = len(l)
    for i in range(0, tam):
        tam1 = len(l[i])
        #for ii in range(0,tam1):
        print("*"*40)
        print(tam1)


def seleccionador_kmeans(l):
    tam = len(l)
    xpro = []
    for i in range(0, tam):

        tam1 = len(l[i])
        x1 = np.array([])
        #for ii in range(0,tam1):
        #print("*"*30)
        #print(i)
        #print(tam1)

        x1 = l[i]
             
            #print(l[i][ii])
            #print("*"*40)
            #print(x1)
        tam2=len(x1)
        if (tam2==1):
            k = 1

            kmeans = KMeans(k)
            # Fitting the input data
            kmeans = kmeans.fit(x1)
            # Getting the cluster labels
            labels = kmeans.predict(x1)
            # Centroid values
            centroids = kmeans.cluster_centers_
            # Comparing with scikit-learn centroids
            #print(C)  # From Scratch
            xpro.append(centroids[0])
        else:
            k = 2
            
            kmeans = KMeans(k)
            # Fitting the input data
            kmeans = kmeans.fit(x1)
            # Getting the cluster labels
            labels = kmeans.predict(x1)
            # Centroid values
            centroids = kmeans.cluster_centers_
            # Comparing with scikit-learn centroids
            #print(C)  # From Scratch
            xpro.append(centroids[randint(0,1)])
           
        '''
        list_two = [4, 5, 6]
        xpro.append(list_two)
        print(x1)
        '''
    return xpro


print(len(seleccionador_kmeans(lis2)))
print(seleccionador_kmeans(lis2))

'''
def rellenador_kmeans(l):
    a = []
    tam = len(l)

    for i in range(1, tam):

        tam1 = (len(l[i]))
        X = np.empty([tam1])
        for ii in range(0,tam1):
            X = l[i][ii]
            kmeans = KMeans(n_clusters=3)
            # Fitting the input data
            kmeans = kmeans.fit(X)
            # Getting the cluster labels
            labels = kmeans.predict(X)
            # Centroid values
            centroids = kmeans.cluster_centers_
            # Comparing with scikit-learn centroids
            #print(C)  # From Scratch
            a.append(l[i][)])
    return centroids
print(rellenador_kmeans(X))
'''
