#Import scikit-learn dataset library
from sklearn import datasets
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import pandas as pd

col_names = ['cliquedistance0', 'cliquedistance1', 'cliquedistance2', 'address0','address1','address2','degree0','degree1','degree2','transitdegree0','transitdegree1','transitdegree2','type0','type1','type2','rir','country','ixp','org','label']


# load dataset
names=['cliquedistance0', 'cliquedistance1', 'cliquedistance2', 'address0','address1','address2','degree0','degree1','degree2','transitdegree0','transitdegree1','transitdegree2','type0','type1','type2','rir','country','ixp','label']

pima = pd.read_csv("./allsample.csv", header=None, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19],
names=names)


# Import train_test_split function
from sklearn.model_selection import train_test_split


# feature_cols = ['cliquedistance0', 'cliquedistance1', 'cliquedistance2', 'address0','address1','address2','degree0','degree1','degree2','transitdegree0','transitdegree1','transitdegree2','type0','type1','type2','rir','country','ixp','org']
feature_cols = names[0:-1]
X = pima[feature_cols] # Features
y = pima.label # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1) 


#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier


clf=RandomForestClassifier(n_estimators=100,max_depth=10)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

CM = confusion_matrix(y_test, y_pred)
TN = CM[0][0]
FN = CM[1][0]
TP = CM[1][1]
FP = CM[0][1]

print("FPR:",FP/(FP+TN))
print("Recall:",metrics.recall_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("F1-score:",metrics.f1_score(y_test, y_pred,average='weighted'))




