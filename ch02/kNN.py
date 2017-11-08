# -*- coding: cp936 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    groups = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return groups, labels



#算法核心
#inX:用于分类的输入向量，即将对其进行分类
#dataSet:训练样本集合
#labels:标签向量
def classify0(inX, dataSet, labels, k):
    # 得到数组的行数。即知道有几个训练数据
    dataSetSize = shape(dataSet)[0]
    print dataSetSize
    # tile:numpy中的函数。tile将原来的一个数组，扩充成了4个一样的数组。diffMat得到了目标与训练数值之间的差值。
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print diffMat
    # 各个元素分别平方
    sqDiffMat = diffMat ** 2
    print sqDiffMat
    # 对应列相乘，即得到了每一个距离的平方
    sqDistances = sqDiffMat.sum(axis=1)
    print sqDistances
    # 开方，得到距离。
    distances = sqDistances ** 0.5
    print distances
    # 升序排列
    sortedDistIndicies = distances.argsort()
    print sortedDistIndicies
    # 选择距离最小的k个点。
    # 字典，key为label，value为出现次数
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        # get是取字典里的元素，如果之前这个voteIlabel是有的，那么就返回字典里这个voteIlabel里的值，如果没有就返回0（后面写的），这行代码的意思就是算离目标点距离最近的k个点的类别，这个点是哪个类别哪个类别就加1
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    print classCount
    # key=operator.itemgetter(1)的意思是按照字典里的第一个排序，{A:1,B:2},要按照第1个（AB是第0个），即‘1’‘2’排序。reverse=True是降序排序
    soredClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print soredClassCount
    # 返回类别最多的类别
    return soredClassCount[0][0]

#sourceLabel = classify0([100, -100], groups, labels, 3)
#print sourceLabel

def file2matrix(filename):
    fr = open(filename, 'r')
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        list_from_line = line.split('\t')
        # returnMat[index, :]：多维切片的写法，表示第index行赋值list_from_line[0:3]
        returnMat[index, :] = list_from_line[0:3]
        #print returnMat
        classLabelVector.append(int(list_from_line[-1]))
        index += 1
    return returnMat, classLabelVector


returnMat, classLabelVector = file2matrix('datingTestSet2.txt')
print returnMat
print classLabelVector

# fig = plt.figure();
#
# ax = fig.add_subplot(111)
# ax.scatter(returnMat[:, 1], returnMat[:, 2], 15.0 * array(classLabelVector), 15.0 * array(classLabelVector))
# plt.show()
def autoNorm(dataSet):
    # 获取数据样本中列最小值
    minVals = dataSet.min(0)
    # 获取数据样本中列最大值
    maxVals = dataSet.max(0)
    # 获取数据样本中列范围值
    ranges = maxVals - minVals
    # 以0填充
    normDataSet = zeros(shape(dataSet))
    m = shape(dataSet)[0]
    # 使用公式 (oldValue-min)/(max-min);这样将所有的特征值归为0-1之间
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

normDataSet, ranges, minVals = autoNorm(returnMat)

print normDataSet

#分类起针对约会网站测试代码
def datingClassTest():
    # 取10%的数据作为测试样本
    hoRatio = 0.10
    datingDataSet, datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataSet)
    m = shape(normMat)[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print "the total error count and error rate is %f,%f,%d" %(float(errorCount), float(errorCount)/float(numTestVecs), int(len(normMat)))


# datingClassTest()

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input('video game rate:'))
    ffMiles = float(raw_input('flier miles earned per years:'))
    iceCream = float(raw_input('liters of ice create consumed per year:'))
    datingDataSet, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataSet)
    inArr = array([ffMiles,percentTats,iceCream])
    inArrNorm = (inArr - minVals)/ranges
    classifierResult = classify0(inArrNorm, normMat, datingLabels, 3)
    print "you will probably like this person:", resultList[classifierResult - 1]

# classifyPerson()

def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect

# returnVect = img2vector('digits/trainingDigits/0_0.txt')
# print returnVect
# print len(returnVect[0])










