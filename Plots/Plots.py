import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_path = '/Users/abs/Work/ForestFiresSpatial/Preprocessing/'

if len(sys.argv) < 2 or (sys.argv[1] != 'sf' and sys.argv[1] != 'sd' and sys.argv[1] != 'la'):
    print ('Incorrect arguments')
    sys.exit()

file, title = '',''
if sys.argv[1] == 'sf':
    file = 'san_francisco_supervised'
    title = 'San Francisco'
elif sys.argv[1] == 'sd':
    file = 'san_diego_supervised'
    title = 'San Diego'
elif sys.argv[1] == 'la':
    file = 'los_angeles_supervised'
    title = 'Los Angeles'

read_file = input_path + file + '.csv'

labels = ['No Fire','Fire']
data = pd.read_csv(read_file)
count_classes = pd.value_counts(data['firecount'], sort = True)
count_classes.plot(kind = 'bar', rot=0)
plt.title(title + " Forest Fire Distribution")
plt.xticks(range(2), labels)
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.show()
plt.savefig(file + '.png')
