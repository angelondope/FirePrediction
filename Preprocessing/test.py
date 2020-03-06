import pandas as pd  
    
# making data frame from csv file  
data = pd.read_csv("san_diego_supervised.csv")  
    
# creating bool series True for NaN values  
year = pd.isnull(data["year"]) 
doy = pd.isnull(data["doy"])
hourmin = pd.isnull(data["hourmin"])
temperature = pd.isnull(data["temperature"])
humidity = pd.isnull(data["humidity"])
pressure = pd.isnull(data["pressure"])
wind = pd.isnull(data["wind"])
firecount = pd.isnull(data["firecount"])

# filtering data  
# displaying data only with Gender = NaN  
#print(data[doy])
#print(data[hourmin])
#print(data[temperature])
#print(data[humidity])
#print(data[pressure])
print(data[wind])
#print(data[firecount])

