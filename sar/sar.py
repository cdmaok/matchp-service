#coding=utf-8

## this file is to build classify model

import features
import numpy as np
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

labelDict = {'s':0,'c':1,'o':2,'l':3,'t':4,'q':5,'m':6,'p':7}
labelReverse = {v:k for k,v in labelDict.items()}

def generatecsv(filepath):
	contents = [line.strip() for line in open(filepath).readlines()]	
	with open(filepath + '.csv','w') as output:
		for line in contents[:]:
			vector = processLine(line)
			vector = [str(e) for e in vector]
			output.write(','.join(vector) + '\n')
	output.close()
	

def processLine(line):
	fields = line.split(' ')
	label = labelDict[fields[0]]
	text = ''.join(fields[1:])
	vector = features.getFV(text)
	v = [label]
	v.extend(vector)
	return v 


def train(filepath):
	data = np.loadtxt(filepath,delimiter=',')
	x = data[:,1:]
	y = data[:,0]
	print x.shape,y.shape
	#model = OneVsOneClassifier(SVC())
	model = GradientBoostingClassifier()
	#model = RandomForestClassifier(criterion='entropy')
	#model = OneVsRestClassifier(LinearSVC(random_state=0))
	scores = cross_validation.cross_val_score(model,x,y, cv=5)
	print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

	model.fit(x,y)
	
	joblib.dump(model, 'sar.model')

	predict = model.predict(x)
	
	print accuracy_score(y,predict)

	#contents = [line.strip() for line in open('/home/guanxinjun/matchp-data/label').readlines()]

	#for index, i in enumerate(y):
	#	if predict[index] != i:
	#		pass
			#print index,labelReverse[predict[index]],contents[index]


	

model = None
def test(text):
	global model
	if model == None: model = joblib.load('/home/guanxinjun/matchpService/sar/sar.model')
	vector = features.getFV(text)
	label = model.predict(vector)[0]
	print label
	return labelReverse[label]






if __name__ == '__main__':
	#generatecsv('/home/guanxinjun/matchp-data/label')
	#train('/home/guanxinjun/matchp-data/label.csv')
	test(u'今天好累啊，饿死了')
