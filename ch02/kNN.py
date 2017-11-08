# -*- coding: cp936 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    groups = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return groups, labels



#�㷨����
#inX:���ڷ������������������������з���
#dataSet:ѵ����������
#labels:��ǩ����
def classify0(inX, dataSet, labels, k):
    # �õ��������������֪���м���ѵ������
    dataSetSize = shape(dataSet)[0]
    print dataSetSize
    # tile:numpy�еĺ�����tile��ԭ����һ�����飬�������4��һ�������顣diffMat�õ���Ŀ����ѵ����ֵ֮��Ĳ�ֵ��
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print diffMat
    # ����Ԫ�طֱ�ƽ��
    sqDiffMat = diffMat ** 2
    print sqDiffMat
    # ��Ӧ����ˣ����õ���ÿһ�������ƽ��
    sqDistances = sqDiffMat.sum(axis=1)
    print sqDistances
    # �������õ����롣
    distances = sqDistances ** 0.5
    print distances
    # ��������
    sortedDistIndicies = distances.argsort()
    print sortedDistIndicies
    # ѡ�������С��k���㡣
    # �ֵ䣬keyΪlabel��valueΪ���ִ���
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        # get��ȡ�ֵ����Ԫ�أ����֮ǰ���voteIlabel���еģ���ô�ͷ����ֵ������voteIlabel���ֵ�����û�оͷ���0������д�ģ������д������˼��������Ŀ�����������k����������������ĸ�����ĸ����ͼ�1
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    print classCount
    # key=operator.itemgetter(1)����˼�ǰ����ֵ���ĵ�һ������{A:1,B:2},Ҫ���յ�1����AB�ǵ�0����������1����2������reverse=True�ǽ�������
    soredClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print soredClassCount
    # ��������������
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
        # returnMat[index, :]����ά��Ƭ��д������ʾ��index�и�ֵlist_from_line[0:3]
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
    # ��ȡ��������������Сֵ
    minVals = dataSet.min(0)
    # ��ȡ���������������ֵ
    maxVals = dataSet.max(0)
    # ��ȡ�����������з�Χֵ
    ranges = maxVals - minVals
    # ��0���
    normDataSet = zeros(shape(dataSet))
    m = shape(dataSet)[0]
    # ʹ�ù�ʽ (oldValue-min)/(max-min);���������е�����ֵ��Ϊ0-1֮��
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

normDataSet, ranges, minVals = autoNorm(returnMat)

print normDataSet

#���������Լ����վ���Դ���
def datingClassTest():
    # ȡ10%��������Ϊ��������
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










