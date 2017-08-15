# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 23:51:00 2017

@author: Harsha SlimShady
"""

import numpy as np
from sklearn import datasets

def distEclud(vecA,vecB):
    return np.sqrt(np.sum(np.power(vecA-vecB,2)))

def randCent(dataSet,k):
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ = np.min(dataSet[:,j])
        rangeJ = np.float(np.max(dataSet[:,j])-minJ)
        centroids[:,j] = minJ + rangeJ*np.random.rand(k,1)
    return centroids

def loadDataSet():
    irisDict = datasets.load_iris()
    return np.mat(irisDict.data)

def kMeans(dataSet,k):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroids = randCent(dataSet,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                distJI = distEclud(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:] = np.mean(ptsInClust,axis=0)
    return centroids,clusterAssment
            


#Running kmeans
   
irisData = loadDataSet()
centroids,classAssment = kMeans(irisData,3)

for i in range(3):
    ptsInClust = irisData[np.nonzero(classAssment[:,0].A==i)[0]]
    print('Cluster %d strentgh : %d'%(i,len(ptsInClust)))
print('\n')
print(classAssment)

            
            
            
            
            
            
            
            
            
            