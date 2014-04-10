#!/usr/bin/env python

from sklearn.externals.six import StringIO  
import pydot 

from sklearn import tree
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix

import numpy as np
import StringIO

def LoadData(trainfile):
	labels = []
	featset = []
	for line in open(trainfile):
		linelist = line.strip().split(',')
		labels += [linelist[0]]
		ftrs = [float(item) for item in linelist[1:len(linelist)]]	
		featset += [ftrs]
	classes = list(set(labels))
	map_dict = {classes[i]:i for i in range(0, len(classes))}
	print map_dict

	class_labels = [map_dict[label] for label in labels]	
	return featset, class_labels


trainfile='/home/yipeiw/Documents/Research-2014spring/vo/prosody.train.txt'
X, Y = LoadData(trainfile)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
Y_predict = clf.predict(X)

#from sklearn.metrics import classification_report
#targetname=['non','contrast','ag']
#print(classification_report(Y, Y_predict, target_names=targetname))

print cross_validation.cross_val_score(clf, X, np.array(Y), cv=5, scoring='accuracy')
print cross_validation.cross_val_score(clf, X, np.array(Y), cv=10, scoring='accuracy')

dot_data = StringIO.StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("../DT_prosody.pdf") 
