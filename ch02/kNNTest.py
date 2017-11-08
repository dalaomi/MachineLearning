# -*- coding: cp936 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir
import kNN

"""
手写数字识别系统测试
"""
def handwritingClassTest():
    hwLabels = []
    traningFileList = listdir('digits/trainingDigits')
    m = len(traningFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = traningFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = kNN.img2vector('digits/trainingDigits/%s' % fileNameStr)
    testFileList = listdir('digits/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = kNN.img2vector('digits/testDigits/%s' % fileNameStr)
        classifierResult = kNN.classify0(vectorUnderTest, trainingMat, hwLabels,3)
        print "the classfier come back with : %d, the real anwser is : %d" % (classifierResult, classNumStr)
        if classifierResult != classNumStr:
            errorCount += 1.0

    print '\nthe total number of errors is : %d' % errorCount
    print '\nthe total rate is : %d' % (errorCount/float(mTest))


handwritingClassTest()



