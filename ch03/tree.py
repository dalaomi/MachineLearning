# -*- coding: cp936 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from math import log

def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        # ���ָ��ʼ���
        prob = float(labelCounts[key])/numEntries
        # ��ũ�صļ��㹫ʽ
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntroy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)

        infoGain = baseEntroy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print sortedClassCount
    return sortedClassCount[0][0]


# ������
def createTree(dataSet, labels):
    # ��ȡ���һ�еı�ǩ�б�
    classList = [example[-1] for example in dataSet]
    print classList
    if classList.count(classList[0]) == len(classList):
        # �ݹ��ս�����1:�����ǩ�б��һ���ĸ������б�����ȣ�����ǩ�б�ֻ��ͬһ����ǩ:���ظ�Ψһ��ǩ
        return classList[0]
    if len(dataSet[0]) == 1:
        # �ݹ��ս�����2:���������������þ������޷��򵥷���Ψһ��ǩ����ȡʣ���ǩ�г��ִ������ķ���
        return majorityCnt(classList)
    # ������ũ�ػ�ȡ��õ�һ����������
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    # ʹ���ֵ䴴����,���ڵ�ʹ�����������ǩ
    myTree = {bestFeatLabel: {}}
    # ɾ���Ѿ�ѡ���������������ǩ
    del(labels[bestFeat])
    feaValue = [example[bestFeat] for example in dataSet]
    uniqKeys = set(feaValue)
    for value in uniqKeys:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree

# ���ຯ��
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    classLabel = ''
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel






