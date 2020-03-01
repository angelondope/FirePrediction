import pandas as pd
import numpy as np

def roundDecimals(read_file):
    raw = pd.read_csv(read_file)
    raw.temperature = np.around(raw.temperature, decimals = 2)
    raw.humidity = np.around(raw.humidity, decimals = 2)
    raw.pressure = np.around(raw.pressure, decimals = 2)
    raw.wind = np.around(raw.wind, decimals = 2)
    raw.to_csv(read_file)

roundDecimals('san_francisco_supervised.csv')
roundDecimals('san_diego_supervised.csv')
roundDecimals('los_angeles_supervised.csv')
