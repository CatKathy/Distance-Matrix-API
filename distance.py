# https://developers.google.com/maps/documentation/distance-matrix/overview


import pandas as pd
import googlemaps

df = pd.read_excel('distance.xlsx')
df

API_key = 'Your API key'
gmaps = googlemaps.Client(key=API_key)


# Create two lists to save data
time_list = []
distance_list = []

for i in range(0,10000): # range should depend on your actual dataset
    lon1 = df.iloc[i,0] # longitude of origins
    lat1 = df.iloc[i,1] # latitude of origins
    lon2 = df.iloc[i,2] # longitude of destinations
    lat2 = df.iloc[i,3] # latitude of destinations

    origin = (lat1, lon1)    
    destination = (lat2, lon2)

    result = gmaps.distance_matrix(origin, destination, mode = 'driving') 
    # mode can be replaced by other methods(e.g. waliking, transit, etc.)
    result_distance = result["rows"][0]["elements"][0]["distance"]["value"]
    result_time = result["rows"][0]["elements"][0]["duration"]["value"]

    print(result_distance)
    print(result_time)
    
    # Append data to lists
    time_list.append(result_time)
    distance_list.append(result_distance)
    

df['time'] = time_list
df['distance'] = distance_list

# Save the file
df.to_excel("distance_final.xlsx")
