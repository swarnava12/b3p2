#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:07:15 2019

@author: pankaz-lab-pc3
"""
#Random Forest Classifier
import pandas as pd
import numpy as np
dataset = pd.read_csv('/home/pankaz-lab-pc3/Desktop/project paper/descriptors.csv')
#dataset1 = dataset[['nHetero', 'ATS0dv', 'ATS3dv', 'ATS4dv', 'ATS0d', 'ATS3Z', 'ATS2m', 'ATS3m', 'ATS4m', 'ATS5m', 'ATS0v', 'ATS4v', 'ATS5se', 'ATS0pe', 'ATS2pe', 'ATS4pe', 'ATS6pe', 'ATS0are', 'ATS2are', 'ATS3are', 'ATS7are', 'ATS8are', 'ATS6i', 'ATS7i', 'ATSC0c', 'ATSC0dv', 'ATSC0d', 'ATSC0v', 'ATSC0pe', 'nBondsS', 'nBondsO', 'nBonds', 'Sare', 'TIC1', 'Kier1', 'LabuteASA', 'SlogP_VSA2', 'MPC2', 'MPC3', 'apol', 'SMR', 'ATS6se', 'p_np']]
dataset1 = dataset[['ATS3m', 'ATS4m', 'ATS0v', 'ATS4v', 'ATS5v', 'ATS6v', 'ATS7v', 'ATS1i', 'ATS2i', 'ATS4i','p_np']]
columns=dataset1.columns
# The labels are in the last column ('Class'). Simply remove it to obtain features columns
features_columns=columns.delete(len(columns)-1)
features=dataset1[features_columns]
labels=dataset1['p_np']
#scaling
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.4, random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  
from sklearn.ensemble import RandomForestClassifier
rf_fit = RandomForestClassifier(n_estimators=5000,criterion="gini",max_depth=5,min_samples_split=2,bootstrap=True,max_features='auto',random_state=42,min_samples_leaf=1,class_weight = {0:0.3,1:0.7})
rf_fit.fit(features_train,labels_train)
print ("\nRandom Forest - Train ConfusionTree-Based Machine Learning ModelsMatrix\n\n",pd.crosstab(labels_train, rf_fit.predict(features_train),rownames =["Actuall"],colnames = ["Predicted"]))
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print ("\nRandom Forest - Train accuracy",round(accuracy_score(labels_train,rf_fit.predict(features_train)),3))
print ("\nRandom Forest - Train Classification Report\n",classification_report( labels_train, rf_fit.predict(features_train)))
print ("\n\nRandom Forest - Test ConfusionMatrix\n\n",pd.crosstab(labels_test, rf_fit.predict(features_test),rownames =["Actuall"],colnames = ["Predicted"]))
print ("\nRandom Forest - Test accuracy",round(accuracy_score(labels_test,rf_fit.predict(features_test)),3))
print ("\nRandom Forest - Test ClassificationReport\n",classification_report( labels_test, rf_fit.predict(features_test)))
#Plot of Variable importance by mean decrease in gini
model_ranks =pd.Series(rf_fit.feature_importances_,index=features_train.columns,name='Importance').sort_values(ascending=False, inplace=False)
model_ranks.index.name = 'Variables'
top_features =
model_ranks.iloc[:31].sort_values(ascending=True,inplace=False)
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
ax = top_features.plot(kind='barh')
= ax.set_title("Variable Importance Plot")
= ax.set_xlabel('Mean decrease in Variance')
= ax.set_yticklabels(top_features.index, fontsize=13)