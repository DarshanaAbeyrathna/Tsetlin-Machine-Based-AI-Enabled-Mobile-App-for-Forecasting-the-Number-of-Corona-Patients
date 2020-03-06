#!/usr/bin/python

import numpy as np
from numpy import save
import pyximport; pyximport.install(setup_args={
                              "include_dirs":np.get_include()},
                            reload_support=True)
import RegressionTM

T = 1000000
s = 2
number_of_clauses = 1000
states = 100
epochs = 5000

df = np.loadtxt("China.txt").astype(dtype=np.float32)

labels = ['C(d-1)',	'C(d)',	'O(d-1)',	'O(d)']

NOofThresholds = 0
maxUniValue = 0
for i in range(len(df[0])-1):
    uniqueValues = list(set(df[:,i]))
    NOofThresholds = NOofThresholds + len(uniqueValues)
    if len(uniqueValues) > maxUniValue:
        maxUniValue = len(uniqueValues)

NewData = np.zeros((len(df), NOofThresholds+1))

m = -1
thresholds = np.empty((len(df[0])-1, maxUniValue))
thresholds.fill(-1)
for i in range(len(df[0])-1):
    uniqueValues = list(set(df[:,i]))
    uniqueValues.sort() 
    NOofuniqueValues = len(uniqueValues)
    for j in range(NOofuniqueValues):
        m += 1
        thresholds[i,j] = uniqueValues[j]
        for k in range(len(df)):
            if df[k,i] <= uniqueValues[j]:
                NewData[k,m] = 1
            else:
                NewData[k,m] = 0
                
NewData[:,NOofThresholds] = df[:,len(df[0])-1]

#train with 80% of data and test with 20%
NOofTestingSamples = df.shape[0]*10//100
NOofTrainingSamples = df.shape[0]-NOofTestingSamples

#training data
X_train = NewData[0:NOofTrainingSamples,0:NewData.shape[1]-1].astype(dtype=np.int32)
y_train = NewData[0:NOofTrainingSamples,NewData.shape[1]-1:NewData.shape[1]].flatten().astype(dtype=np.float32)
rows, number_of_features = X_train.shape

max_target = (max(y_train))
min_target = (min(y_train))

#testing data
X_test = NewData[NOofTrainingSamples:NewData.shape[0],0:NewData.shape[1]-1].astype(dtype=np.int32)
y_test = NewData[NOofTrainingSamples:NewData.shape[0],NewData.shape[1]-1:NewData.shape[1]].flatten().astype(dtype=np.float32)

#call and train the regression tsetlin machine
tsetlin_machine = RegressionTM.TsetlinMachine(number_of_clauses, number_of_features, states, s, T, max_target, min_target)
tsetlin_machine.fit(X_train, y_train, y_train.shape[0], epochs=epochs)

TAstates = np.zeros((number_of_clauses, (number_of_features*2)), dtype=np.int32)
Weights = np.zeros((number_of_clauses, 1), dtype=np.int32)
suportive = np.zeros((7, 1), dtype=np.float32)
suportive[0,0], suportive[1,0], suportive[2,0] = T, max_target, min_target
suportive[3,0], suportive[4,0], suportive[5,0] = NOofTrainingSamples, tsetlin_machine.evaluate(X_train, y_train, y_train.shape[0]), tsetlin_machine.evaluate(X_test, y_test, y_test.shape[0])
suportive[6,0] = df.shape[1] - 1

for clause in range(number_of_clauses):
    Weights[clause] = tsetlin_machine.get_weights(clause)
    feature_index = 0
    for feature in range(number_of_features):
        tatype = 0 #tatype 1 is negated, 0 is original
        if tsetlin_machine.get_state(clause,feature,tatype) > states:
            TAstates[clause, feature_index] = 1
        else:
            TAstates[clause, feature_index] = 0
            
        tatype = 1 #tatype 1 is negated, 0 is original
        if tsetlin_machine.get_state(clause,feature,tatype) > states:
            TAstates[clause, feature_index+1] = 1
        else:
            TAstates[clause, feature_index+1] = 0
            
        feature_index += 2
    
TMextracts = np.hstack((Weights,TAstates))
save('TMextractsChina.npy', TMextracts)
save('RegSupChina.npy', suportive)
save('ThredsChina.npy', thresholds)
save('LabsChina.npy', labels)


for i in range(NOofTestingSamples):
    print ("out:", tsetlin_machine.predict(X_test[i]))
print ("MAE on training data:", tsetlin_machine.evaluate(X_train, y_train, y_train.shape[0]))
print ("MAE on test data:", tsetlin_machine.evaluate(X_test, y_test, y_test.shape[0]))

    