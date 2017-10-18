import sys
import numpy as np
#注意数据类型的转换
# sys.path.append('data/')

# data = []
# # for line in open(r"C:\Users\Asdil\Desktop\pythonProject\MyKmeans\data\iris.data"):
# #     data.append(line)
# #     print(line)
# data = [line.split() for line in open(r'C:\Users\Asdil\Desktop\pythonProject\MyKmeans\data\iris.data').readlines()]
#
# # lists=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# # lists= map(int, lists)
# # temp = []
# # for i in lists:
# #     temp.append(i)
# # print(temp)
#
# data2 = ['1','3.2','2']
# data2 = map(eval, data2)
# print(data2)



# data=[]
# with open(r'C:\Users\Asdil\Desktop\pythonProject\MyKmeans\data\iris.data') as f:
#     for line in f:
#         data.append(list(map(float,line.split())))
#     print(data)
# x = np.max(data)
# print(x)
#
# # data2=np.loadtxt(r'C:\Users\Asdil\Desktop\pythonProject\MyKmeans\data\iris.data', skiprows=1)
# # data2=np.loadtxt(r'C:\Users\Asdil\Desktop\pythonProject\MyKmeans\data\iris.csv', skiprows=0, delimiter=',',usecols=(0,1,2))
# data2=np.loadtxt("data/iris.csv", skiprows=0, delimiter=',',usecols=(0,1,2))
# print(data2)
# print(len(data2))
#
# c = np.array([[1, 90, 3, 4],[4, 5, 11, 7], [7, 0, 9, 10]])
# print(np.max(c, axis = 0))
# print(np.argmax(c, axis = 0))
# print(np.max(c, axis = 1))
#
# thamaxs=np.max(c, axis = 0)
#
# dd=np.where(c[:,0]==thamaxs[0])

a = np.array([[1, 2],[3,4],[5,7]])
print(np.mean(a,axis=0))

print(dd)
# print(np.idxmin(c,axis=0))
# print(np.max(c))
# print(np.where(c==c.max()))
