import sys
import pandas as pd
import numpy as np

read_file, write_file, count = '', '', sys.argv[2]
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
    write_file  = file_split[0] + '_' + file_split[1] + '_random.csv'


raw = pd.read_csv(read_file)
raw = raw.sample(n = int(count), random_state = 1, axis = 0)
raw.to_csv(write_file)