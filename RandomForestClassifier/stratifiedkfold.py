import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

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
model = RandomForestClassifier(n_estimators=10, class_weight = 'balanced')

x, y = train.iloc[:,4:8], train.iloc[:,-1]
skf = StratifiedKFold(n_splits = 5, random_state = None)
skf.get_n_splits(x, y)
accuracy = []
precision = []
recall = []
f1score = []

print(train_set)

for train_index, test_index in skf.split(x, y):
    x_train, x_test = x.iloc[train_index], x.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    accuracy.append(accuracy_score(y_test, prediction))
    precision.append(precision_score(y_test, prediction, pos_label='T'))
    recall.append(recall_score(y_test, prediction, pos_label='T'))
    f1score.append(f1_score(y_test, prediction, pos_label='T'))

print ('accuracy : ', np.array(accuracy).mean())
print ('precision : ', np.array(precision).mean())
print ('recall : ', np.array(recall).mean())
print ('f1 Score : ', np.array(f1score).mean())
print()