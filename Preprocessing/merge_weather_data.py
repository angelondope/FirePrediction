import pandas as pd
import numpy as np
import sys


main = pd.read_csv('temperature_f.csv')
temp = pd.read_csv('temperature_f.csv')
humi = pd.read_csv('humidity_f.csv')
wind = pd.read_csv('wind_speed_f.csv')
pres = pd.read_csv('pressure_f.csv')
main.drop(columns=['Unnamed: 0','San Francisco','Los Angeles','San Diego'], inplace=True)

main['temperature'] = temp['San Francisco']
main['humidity'] = humi['San Francisco']
main['wind'] = wind['San Francisco']
main['pressure'] = pres['San Francisco']
main.reset_index(drop=True, inplace=True)
main.to_csv('san_francisco_weather.csv')


main['temperature'] = temp['Los Angeles']
main['humidity'] = humi['Los Angeles']
main['wind'] = wind['Los Angeles']
main['pressure'] = pres['Los Angeles']
main.reset_index(drop=True, inplace=True)
main.to_csv('los_angeles_weather.csv')

main['temperature'] = temp['San Diego']
main['humidity'] = humi['San Diego']
main['wind'] = wind['San Diego']
main['pressure'] = pres['San Diego']
main.reset_index(drop=True, inplace=True)
main.to_csv('san_diego_weather.csv')