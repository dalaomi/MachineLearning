# -*- coding: cp936 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from math import log
import bayes

listOfPosts, listClasses = bayes.loadDataSet()
print listOfPosts
print listClasses


myVocabList = bayes.createVocabList(listOfPosts)
print myVocabList

trainMat = []
for postinDoc in listOfPosts:
    trainMat.append(bayes.setOfWord2Vec(myVocabList, postinDoc))

print trainMat


p0Vect, p1Vect, pAbusive = bayes.trainNB0(trainMat, listClasses)
print p0Vect, p1Vect, pAbusive


bayes.testingNB()
