# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 
# for 2 and 3, you will need to enable the google places API
# you may find this page useful to learn about different findinging nearby places https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/
# https://googlemaps.github.io/google-maps-services-python/docs/ 


import importlib
import os
import googlemaps

os.chdir('E:/mine/academics_career/Github_keys')
imported_items = importlib.import_module('start_google')
gmaps = imported_items.client

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

embassies = [[38.917228,-77.0522365], \
	[38.9076502, -77.0370427], \
	[38.916944, -77.048739]]

distance = gmaps.distance_matrix(whitehouse, embassies)
all_distances = []
emb_dict = {}

for i in range(3):
    emb = distance["destination_addresses"][i]
    d = float(distance['rows'][0]['elements'][i]['distance']['text'].split()[0])
    emb_dict[emb] = d
    
min_val = min(emb_dict.values())
min_emb = min(emb_dict)
all_nearby_morning_cafe = gmaps.places_nearby(embassies[1], rank_by = "distance", type = "cafe")
all_nearby_morning_cafe['results'][0]["name"]

bars = {}
all_nearby_bars = gmaps.places_nearby(embassies[1], rank_by = "distance", type = "bar")
len(all_nearby_morning_cafe['results'])

for i in range(len(all_nearby_morning_cafe['results'])):
    name = all_nearby_bars["results"][i]["name"]
    rating = all_nearby_bars["results"][i]["rating"]
    bars[name] = rating
    

print(max(bars, key = bars.get))
