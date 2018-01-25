from numpy import  *
import KNN


#读入文件得到分类后的数据集和标签
#datingDataMat,datingLabels = KNN.file2matrix('C:\\Users\\Lenovo\\Desktop\\datingTestSet2.txt')

'''
#用散点图表示原始数据
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
#要import numpy模块，不然会报错
ax.scatter(datingDataMat[:,0], datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
'''

'''
normMat, ranges, minVals = KNN.autoNorm(datingDataMat)
print(normMat)
print(ranges)
print(minVals)

'''
#KNN.datingClassTest()
KNN.classifyPerson()

