#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Peter
"""


#import these packages to aid with creating svm model
import pandas as pd
import pandas.util.testing as tm
import seaborn as sns
import numpy as np
from sklearn.svm import SVC
import pickle
from sklearn.model_selection import train_test_split
%matplotlib inline


#create X and y from dataset
names_by_gender = pd.read_csv("data/gender_names_final.csv").iloc[:,2:]
y = names_by_gender["Gender"]
X = names_by_gender.loc[:, "0":"24"]


#create training and testing data from X and y
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.4, random_state=0)


#fit model and save to file
clf = SVC(gamma = 2, C =1).fit(X_train, y_train)
filename = 'gender_name_svc.sav'
#pickle.dump(clf, open(filename, 'wb'))


#load file and get testing score
clf = pickle.load(open('gender_name_svc.sav', 'rb'))
clf_score = clf.score(X_test, y_test)

print(clf_score)
#output is 0.5569362395599918
                


