import math
import numpy as np
import pandas as pd
df = pd.read_excel("distance.xlsx")

#def haversine(coord1: object, coord2: object):
def haversine(lon1, lat1, lon2, lat2):
    import math


    R = 6371000  # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    km = meters / 1000.0  # output distance in kilometers

    meters = round(meters, 3)
    km = round(km, 3)
    
    return km
  
  
  dist = []
  
  for i in range(0,569):
    lon1 = df.iloc[i,0]
    lat1 = df.iloc[i,1]
    lon2 = df.iloc[i,2]
    lat2 = df.iloc[i,3]
    
    result = haversine(lon1, lat1, lon2, lat2)
#    print(result)
    
    dist.append(result)
    
df['distance'] = dist

df.to_excel("distance_new.xlsx")
