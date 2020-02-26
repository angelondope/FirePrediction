import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

read_file = ''
input_path = '/Users/abs/Work/ForestFiresSpatial/Preprocessing/'

if len(sys.argv) < 2 or (sys.argv[1] != 'sf' and sys.argv[1] != 'sd' and sys.argv[1] != 'la'):
    print ('Incorrect arguments')
    sys.exit()
else:
    if sys.argv[1] == 'sf':
        read_file = input_path + 'san_francisco_supervised.csv'
    elif sys.argv[1] == 'sd':
        read_file = input_path + 'san_diego_supervised.csv'
    elif sys.argv[1] == 'la':
        read_file = input_path + 'los_angeles_supervised.csv'

raw = pd.read_csv(read_file)

raw.temperature = np.around(raw.temperature, decimals = 2)
raw.humidity = np.around(raw.humidity, decimals = 2)
raw.pressure = np.around(raw.pressure, decimals = 2)
raw.wind = np.around(raw.wind, decimals = 2)

x,y = raw.iloc[:,3:6], raw.iloc[:,-1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1)

model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)
prediction = model.predict(x_test)

print ('accuracy : ' + str(accuracy_score(y_test, prediction)))
print ('precision : ' + str(precision_score(y_test, prediction, pos_label='T')))
print ('recall : ' + str(recall_score(y_test, prediction, pos_label='T')))
print ('f1 Score : ' + str(f1_score(y_test, prediction, pos_label='T')))
