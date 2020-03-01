import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

read_file, train_set, test_set = '', '', ''
input_path = '/Users/abs/Work/ForestFiresSpatial/Sampling/'

if len(sys.argv) < 4 or (sys.argv[1] != 'sf' and sys.argv[1] != 'sd' and sys.argv[1] != 'la'):
    print ('Incorrect arguments')
    sys.exit()
else:
    if sys.argv[1] == 'sf':
        read_file = input_path + 'san_francisco'
    elif sys.argv[1] == 'sd':
        read_file = input_path + 'san_diego'
    elif sys.argv[1] == 'la':
        read_file = input_path + 'los_angeles'

    if sys.argv[2] == 'stratified':
        train_set = read_file + '_stratified.csv'
    elif sys.argv[2] == 'reservoir':
        train_set = read_file + '_reservoir.csv'
    else:
        train_set = read_file + '_random.csv'

    if sys.argv[3] == 'stratified':
        test_set = read_file + '_stratified.csv'
    elif sys.argv[3] == 'reservoir':
        test_set = read_file + '_reservoir.csv'
    else:
        test_set = read_file + '_random.csv'

train = pd.read_csv(train_set)
test = pd.read_csv(test_set)

x_train, x_test, y_train, y_test = train.iloc[:,4:8], test.iloc[:,4:8], train.iloc[:,-1], test.iloc[:,-1]

model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print (train_set + ' : ' + test_set)
print ('accuracy : ' + str(accuracy_score(y_test, prediction)))
print ('precision : ' + str(precision_score(y_test, prediction, pos_label='T')))
print ('recall : ' + str(recall_score(y_test, prediction, pos_label='T')))
print ('f1 Score : ' + str(f1_score(y_test, prediction, pos_label='T')))
