import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = pd.read_csv('data.csv')
x, y = raw_data['x'], raw_data['y']
plt.plot(x, y)
plt.title('Oversample Fire vs F1 Score')
plt.xlabel('Oversample By')
plt.ylabel('F1 Score')
plt.show()