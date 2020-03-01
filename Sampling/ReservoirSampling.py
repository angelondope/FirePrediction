import sys
import pandas as pd
import numpy as np

read_file, write_file, count = '', '', sys.argv[2]
count = int(count)
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
    write_file  = file_split[0] + '_' + file_split[1] + '_reservoir.csv'

readFile = open(read_file,'r')
reservoir = []     

i = 0
for line in readFile :
	if i < count :
		reservoir.append(line)
	else :
		rand = np.random.randint(1,i + 1)
		if rand < count :
			reservoir[rand] = line
	i += 1
readFile.close()

writeFile = open(write_file,'w')
for i in reservoir :
	writeFile.write(i)
writeFile.close()

raw = pd.read_csv(write_file)
raw = raw[['year','doy','hourmin','temperature','humidity','pressure','wind','firecount']]
raw.temperature = np.around(raw.temperature, decimals = 2)
raw.humidity = np.around(raw.humidity, decimals = 2)
raw.pressure = np.around(raw.pressure, decimals = 2)
raw.wind = np.around(raw.wind, decimals = 2)
raw.to_csv(write_file)