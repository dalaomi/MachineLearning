# -*- coding: cp936 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from math import log
import bayes

postingList, classVec = bayes.loadDataSet()
print postingList, classVec


vocabSet = bayes.createVocabList(postingList)
print vocabSet
print postingList[3]
returnVec = bayes.setOfWord2Vec(vocabSet, postingList[3])
print returnVec

