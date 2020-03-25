import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, precision_recall_curve, classification_report
import matplotlib.pyplot as plt

read_file, train_set = '', ''
input_path = '/Users/abs/Work/ForestFiresSpatial/Sampling/'

if len(sys.argv) < 3 or (sys.argv[1] != 'sf' and sys.argv[1] != 'sd' and sys.argv[1] != 'la'):
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

train = pd.read_csv(train_set)
x_train, x_test, y_train, y_test = train_test_split(train.iloc[:,4:8], train.iloc[:,-1], test_size = 0.2, random_state = 2, shuffle = True)
model = SVC(kernel = 'rbf', C = 15, gamma = 'auto', class_weight = 'balanced')
model.fit(x_train, y_train)
prediction = model.predict(x_test)
print(train_set)
# print ('accuracy : ' + str(accuracy_score(y_test, prediction)))
# print ('precision : ' + str(precision_score(y_test, prediction, pos_label='T')))
# print ('recall : ' + str(recall_score(y_test, prediction, pos_label='T')))
# print ('f1 Score : ' + str(f1_score(y_test, prediction, pos_label='T')))

print(classification_report(y_test, prediction, labels = ['T','F']))
print()