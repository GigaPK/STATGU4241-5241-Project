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

#plot learning curve
skplt.estimators.plot_learning_curve(clf_rbf, X_train, y_train)
plt.title("Learning Curve of the SVC with RBF Kernel")
plt.show()

#tune gamma, using this selection
gammas = [1, 0.1, 0.01, 0.001, 0.0001]


#create function that creates svm rbf model, saves model in pickle
#and outputs testing scoe

def train_and_test_rbf_svc(gamma_set):
    for gamma in gamma_set:
        clf_rbf = SVC(gamma = gamma, C =1, kernel = "rbf").fit(X_train, y_train)
        filename = "gender_name_svc_rbf_g" + str(gamma) + ".sav"
        pickle.dump(clf_rbf, open(filename, 'wb'))
        clf_rbf_score = clf_rbf.score(X_test, y_test)
        print(f'The score of the rbf svm model with gamma = {gamma}, is {clf_rbf_score}')
         
          
train_and_test_rbf_svc(gammas)

#here is the output:
#The score of the rbf svm model with gamma = 1, is 0.5689040537787737
#The score of the rbf svm model with gamma = 0.1, is 0.6258402933387656
#The score of the rbf svm model with gamma = 0.01, is 0.6896856114619406
#The score of the rbf svm model with gamma = 0.001, is 0.6352787397297481
#The score of the rbf svm model with gamma = 0.0001, is 0.6120900387044205


#create linear kernal SVC with default values
clf_lin = SVC(C =1, kernel = "linear").fit(X_train, y_train)

#save linear kernal SVC to memory 
pickle.dump(clf_lin, open('gender_name_svc_lin.sav', 'wb'))

#if already initialized the file, start here and reload the linear model
clf_lin = pickle.load(open('gender_name_svc_lin.sav', 'rb'))

clf_lin_score = clf_lin.score(X_test, y_test)
clf_lin_score
#output is: 0.6120391118354044


#create 2nd degree polynomial SVC with default values
clf_poly2 = SVC(C =1, kernel = "poly", degree = 2, coef0 = 0.0).fit(X_train, y_train)

#save 2nd deg poly kernal SVC to memory 
pickle.dump(clf_poly2, open('gender_name_svc_poly2.sav', 'wb'))

#if already initialized the file, start here and reload the polynomial model
clf_poly2 = pickle.load(open('gender_name_svc_poly2.sav', 'rb'))

clf_poly2_score = clf_poly2.score(X_test, y_test)
clf_poly2_score

#output is 0.6136687716439193


