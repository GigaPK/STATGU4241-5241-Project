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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import validation_curve
%matplotlib inline


#create X and y from dataset
names_by_gender = pd.read_csv("data/gender_names_final.csv").iloc[:,2:]
y = names_by_gender["Gender"]
X = names_by_gender.loc[:, "0":"24"]


#create training and testing data from X and y
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.4, random_state=0)


#Set depths of which to tune
depths = [3,5,10,20,30]

#fit models using depths and make vaidation curves
train_scores,test_scores = validation_curve(RandomForestClassifier(), 
                                            X_train, y_train,param_name = 'max_depth', 
                                            param_range = depths, cv = 3, scoring = 'accuracy')

#save mean training and testing scores
mean_train_scores = train_scores.mean(axis = 1)
mean_test_scores = test_scores.mean(axis = 1)


print(mean_train_scores)
# output is [0.60776813 0.63918467 0.75682146 0.92736049 0.96387547]

print(mean_test_scores)
# output is [0.60773418 0.63599333 0.73192922 0.7572911  0.74331436]
