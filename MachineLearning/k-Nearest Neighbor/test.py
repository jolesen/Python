import KNN

group, labels = KNN.createDataSet()
print(KNN.classify0([0,0], group, labels, 3))
