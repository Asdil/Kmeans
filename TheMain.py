import numpy as np
from numpy.matlib import repmat
import matplotlib.pyplot as plt
#注意数据类型的转换
from funcation import mykmeans
def main():
    k = 3  # 类簇个数

    # data2np.loadtxt("data/iris.csv", skiprows=0, delimiter=',',usecols=(0,1,2))
    data = np.loadtxt("data/iris.csv", skiprows=0, delimiter=',', usecols=(0, 1, 2))  # usecols表示读取列数
    # np.savetxt('new.csv', data, delimiter=',')
    lab = data[:, -1]
    print(lab)  # 读取类标签
    data = data[:, 0:-1]  # 读取数据
    print("矩阵维度是:%d,%d" % (data.shape[0], data.shape[1]))
    dataNumber = data.shape[0]  # 数据个数
    dataRows = data.shape[1]  # 维度
    theMax = np.max(data, axis=0)  # 获取每个维度最大值
    theMin = np.min(data, axis=0)  # 获取每个维度最小值
    c = theMax - theMin
    center = repmat(theMin, k, 1)  # 将中心点变为矩阵
    center=mykmeans.initeCenter(k,dataRows,dataNumber,theMax,theMin)
    oldCenter=np.array(np.zeros((k,dataRows)))
    thresholtimes=100
    marked=mykmeans.clustering(k, data, dataNumber, center, oldCenter, thresholtimes)
    plt.figure(figsize=(7, 7))
    plt.scatter(data[:, 0], data[:, 1], c=marked)
    plt.show()
if __name__ == '__main__':
    main()