# -*- coding: cp936 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from math import log
import tree
import treePlotter


myDataSet, labels = tree.createDataSet()
shannonEnt = tree.calcShannonEnt(myDataSet)
print myDataSet


retDataSet = tree.splitDataSet(myDataSet, 1, 1)
#print retDataSet



tree.chooseBestFeatureToSplit(myDataSet)


myList = [0, 1, 1, 1, 0, 1]
myList1 = [1, 0, 0, 0, 1, 0]
tree.majorityCnt(myList)
tree.majorityCnt(myList1)


# myTree = tree.createTree(myDataSet, labels)
# print myTree

#treePlotter.createPlot()


myTree = treePlotter.retrieveTree(0)
print myTree
print '-----'
cc = tree.classify(myTree, labels, [1, 1])
print cc

cc = tree.classify(myTree, labels, [1,0])
print cc


cc = tree.classify(myTree, labels, [0])
print cc


