# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:12:55 2017

@author: adityan
"""

import pandas as pd
import sklearn

#Read the data from the csv file
f = open("spambase.data")
f.readline()  # skipping the header
data = pd.read_csv(f)


#Divide to training and testing data sets
x_features = data.iloc[500:3000, :-1]
x_label = data.iloc[500:3000, -1]

#Testing data
#Split the data
#split and test for remaining data also
x_test_features = data.iloc[1000:-1, :-1]
x_test_label = data.iloc[1000:-1, -1]



#decision tree classifier
#you can use any other classifier as Randomforest,Knn etc
clf = tree.DecisionTreeClassifier()
clf= clf.fit(x_features, x_label)
predictions = clf.predict(x_test_features)

#accuracy definition

print(predictions)
from sklearn.metrics import accuracy_score
print("Accuracy:",accuracy_score(x_test_label, predictions) * 100)