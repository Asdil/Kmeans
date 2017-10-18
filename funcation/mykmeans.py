import numpy as np
from numpy.matlib import repmat
def initeCenter(k,dataRows,dataNumber,theMax,theMin):
    randomK = np.random.random(size=dataRows*k)  #生成k个0-1随机数
    randomK=randomK.reshape((k,dataRows))
    # randomK=repmat(randomK, dataRows,1 )     #一个向量重复变成矩阵
    # randomK=randomK.T                   #矩阵转置，注意每一列是相同的
    center=(randomK*theMin)+theMin                 #生成初始聚类中心
    print("初始聚类中心为：")
    print(center)                      #打印聚类中心
    return center
def findNewCenter(k,data,dataNumber,center):
    centerDist = np.ones((dataNumber, k))
    for i in range(0,k):
        dist=(data-center[i,:])**2
        dist=np.sum(dist,axis=1)
        #dist=np.power(dist,0.5)
        dist=np.sqrt(dist)
        centerDist[:,i]=dist
    marked=np.argmin(centerDist,axis=1)
    print(marked)
    oldCenter=np.array(center)
    for i in range(0, k):
        index=np.where(marked==i)
        newCenter=data[index,:]
        newCenter=np.mean(newCenter, axis=1)
        center[i,:]=newCenter
    return marked,center,oldCenter
def clustering(k,data,dataNumber,center,oldCenter,thresholtimes):
    #初始化
    thresholdError=0.01       #中心点迭代阈值
    realError=(center - oldCenter)
    realError=realError ** 2
    realError = np.sum(realError,axis=1 )
    realError = np.sqrt(realError)
    realError = sum(realError)
    runingTimes=1
    #循环
    while (realError>thresholdError and runingTimes<thresholtimes):
        marked,center, oldCenter=findNewCenter(k,data,dataNumber,center)
        realError = (center - oldCenter)
        realError = realError ** 2
        realError = np.sum(realError, axis=1)
        realError = np.sqrt(realError)
        realError = sum(realError)
        runingTimes +=1
    print(runingTimes)
    return marked


