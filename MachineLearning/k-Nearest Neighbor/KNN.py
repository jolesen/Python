from numpy import *
import operator
from os import listdir

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

#分类器：k-邻近算法，计算距离，选择距离最小的k个点，对点进行排序
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in list(range(k)):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    #python3中iteritems()为items()
    return sortedClassCount[0][0]


#将文件的数据格式改编为分类器可以接受的格式
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #得到文件行数
    returnMat = zeros((numberOfLines,3))        #创建返回的NumPy矩阵
    classLabelVector = []                       #解析文件数据到列表
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

#由于权重不同，要进行归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)   #每列最小值
    maxVals = dataSet.max(0)    #最大值
    ranges = maxVals - minVals  #
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #特征值相除
    return normDataSet, ranges, minVals

#测试算法
def datingClassTest():
    hoRatio = 0.10      #用10%作为测试样本
    datingDataMat,datingLabels = file2matrix('C:\\Users\\Lenovo\\Desktop\\datingTestSet2.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat) #读取并完成了归一化特征值

    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio) #确定测试部分
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("分类器返回结果: %d, 真实的结果是: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print ("错误率为: %f" % (errorCount/float(numTestVecs)))
    print("错误个数:",errorCount)


#应用程序
def classifyPerson():
    resultList = ['一点兴趣也没有', '有点兴趣', '非常中意']
    percentTate = float(input("玩游戏的时间比例为多少个百分比？："))
    ffMiles = float(input("每年的常飞里程是？："))
    ice_Cream = float(input("每年吃了多少公升的冰淇淋？："))

    datingDataMat, datingLabels = file2matrix('C:\\Users\\Lenovo\\Desktop\\datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat) #归一化特征值
    inArr = array([ffMiles, percentTate, ice_Cream])

    classifierResult = classify0((inArr - minVals)/ranges,normMat,datingLabels,3) #调用分类器

    print("你对这个人的感受很可能是：",resultList[classifierResult - 1])


#将32x32的二进制图像转换为1x1024的向量
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in list(range(32)):
        lineStr = fr.readline()
        for j in list(range(32)):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect



#手写数字识别系统的测试代码
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('C:\\Users\\Lenovo\\Desktop\\trainingDigits')           #获取训练目录内容
    m = len(trainingFileList) #得到目录内一共有多少文件
    trainingMat = zeros((m,1024))  #m列1024行训练矩阵，每列存储一个图像
    for i in list(range(m)):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0]) #获得图像代表的数字的真实结果
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('C:\\Users\\Lenovo\\Desktop\\trainingDigits/%s' % fileNameStr) #载入图像

    testFileList = listdir('C:\\Users\\Lenovo\\Desktop\\testDigits')        #循环迭代读入测试数据
    errorCount = 0.0
    mTest = len(testFileList) #得到测试集的总数
    for i in list(range(mTest)):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0]) #真实结果

        #将32x32的二进制图像转换为1x1024的向量
        vectorUnderTest = img2vector('C:\\Users\\Lenovo\\Desktop\\testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 9) #带入分类器，得到分类器的返回结果
        print("分类器返回结果: %d, 真实结果是: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0

    print("\n错误总数是 is: %d" % errorCount)
    print("\n错误率为: %f" % (errorCount/float(mTest)))




