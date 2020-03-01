import sys
import pandas as pd
import numpy as np

read_file, write_file, count, num, denom = '', '', sys.argv[2], sys.argv[3], sys.argv[4]
frac = float(num)/float(denom)
count = float(count)
input_path = '/Users/abs/Work/ForestFiresSpatial/Preprocessing/'

if len(sys.argv) < 3 or (sys.argv[1] != 'sf' and sys.argv[1] != 'sd' and sys.argv[1] != 'la'):
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
    write_file  = file_split[0] + '_' + file_split[1] + '_stratified.csv'


raw = pd.read_csv(read_file)
df1 = raw[raw.firecount == 'T']
df2 = raw[raw.firecount == 'F']
df1 = df1.sample(n = min(int(count * frac), len(df1)), random_state = 1, axis = 0)
df2 = df2.sample(n = min(int((1-frac) * count), len(df2)), random_state = 1, axis = 0)
df1 = df1.append(df2, ignore_index = True)
df1.to_csv(write_file)