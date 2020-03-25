import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, precision_recall_curve, classification_report

read_file, write_file, count, over = '', '', sys.argv[2], sys.argv[3]
count = float(count)
over = int(over)
input_path = '/Users/abs/Work/ForestFiresSpatial/Preprocessing/'

if len(sys.argv) < 2 or (sys.argv[1] != 'sf' and sys.argv[1] != 'sd' and sys.argv[1] != 'la'):
    print ('Incorrect arguments')
    sys.exit()
else:
    file = ''
    if sys.argv[1] == 'sf':
        file = 'san_francisco_supervised.csv'
    elif sys.argv[1] == 'sd':
        file = 'san_diego_supervised.csv'
    elif sys.argv[1] == 'la':
        file = 'los_angeles_supervised.csv'

    read_file = input_path + file
    file_split = file.split('_');
    write_file  = file_split[0] + '_' + file_split[1] + '_oversample.csv'


rfile = open(read_file,'r')
wfile = open(write_file,'w')

order_iter = 0

for line in rfile:
    words = line.split(',')

    if order_iter != 0:
        words[8] = 'T\n'
        order_iter -= 1
    elif words[8] == 'T\n':
        order_iter = over - 1

    wfile.write(words[0] + ',' + words[1] + ',' + words[2] + ',' + words[3] + ',' + words[4] + ',' + words[5] + ',' + words[6] + ',' + words[7] + ',' + words[8])
    
rfile.close()
wfile.close()

raw = pd.read_csv(write_file)
df1 = raw[raw.firecount == 'T']
df2 = raw[raw.firecount == 'F']

frac = float(len(df1))/float(len(df2) + len(df1))
df1 = df1.sample(n = min(int(count * frac), len(df1)), random_state = 1, axis = 0)
df2 = df2.sample(n = min(int((1-frac) * count), len(df2)), random_state = 1, axis = 0)
df1 = df1.append(df2, ignore_index = True)
df1 = df1[['year','doy','hourmin','temperature','humidity','pressure','wind','firecount']]
df1 = df1.sample(frac = 1)
df1.to_csv(write_file)

train = df1
model = SVC(kernel = 'rbf', C = 15, gamma = 'auto', class_weight = 'balanced')

x_train, x_test, y_train, y_test = train_test_split(train.iloc[:,3:7], train.iloc[:,-1], test_size = 0.2, random_state = 2, shuffle = True)
model.fit(x_train, y_train)
pred = model.predict(x_test)
print(classification_report(y_test, pred, ['T', 'F']))

x, y = train.iloc[:,3:7], train.iloc[:,-1]
skf = StratifiedKFold(n_splits = 10, random_state = None)
skf.get_n_splits(x, y)

accuracy = []
precision = []
recall = []
f1score = []

for train_index, test_index in skf.split(x, y):
    x_train, x_test = x.iloc[train_index], x.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    accuracy.append(accuracy_score(y_test, prediction))
    precision.append(precision_score(y_test, prediction, pos_label='T'))
    recall.append(recall_score(y_test, prediction, pos_label='T'))
    f1score.append(f1_score(y_test, prediction, pos_label='T'))

print('SVM')
print ('accuracy : ', np.array(accuracy).mean())
print ('precision : ', np.array(precision).mean())
print ('recall : ', np.array(recall).mean())
print ('f1 Score : ', np.array(f1score).mean())
print ()