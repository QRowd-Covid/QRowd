from flask import Flask, render_template, request
from dotenv import load_dotenv
import urllib.request, urllib.parse, urllib.error
import http.client
import geocoder
import json
from json import loads
import os
import requests

load_dotenv()
MAPS_TOKEN = os.getenv('MAPS_TOKEN')
DATASET_ID = os.getenv('DATASET_ID')
MAPS_USER = os.getenv('MAPS_USER')


conn = http.client.HTTPSConnection('api.mapbox.com')

conn.request('GET', '/datasets/v1/' + MAPS_USER + '/' + DATASET_ID + '/features?access_token=' + MAPS_TOKEN)

# Decode UTF8 responses
res = conn.getresponse()
data = res.read().decode("utf-8")
# Create JSON object from data
try:
    js = json.loads(data)
except:
    js = None
# Check JSON object for errors (ie. invalid WORD)
if not js:
    print('error')
# 'https://api.mapbox.com/datasets/v1/nishantbalaji/ckeq2oto816oe28k48h74h0h8?access_token=' + MAPS_TOKEN
#print(js)


feature_id = '3aee9878de75607db4ebe53db9681a3b'
type = 'Point'
body = {
  "id": "01",
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      -121.158035,
      38.648559
    ]
  },
  "properties": {
    "prop0": "value0"
  }
}

# ????
createurl = "https://api.mapbox.com/datasets/v1/" + MAPS_USER + "?access_token=" + MAPS_TOKEN
resp = requests.get(createurl)
print(resp.json())
print("\n")

# create another dataset
#req={
  #"name": "foo123",
#  "description": "bar123"
#}
#reqjosn = json.dumps(req)
#resp = requests.post(requrl, data=reqjosn)
#print(resp.json())

# get a specific dataset
geturl = "https://api.mapbox.com/datasets/v1/" + MAPS_USER + "/" + DATASET_ID + "?access_token=" + MAPS_TOKEN
resp = requests.get(geturl)
print(resp.json())
print("\n")

# get specific dataset's features
featurl = "https://api.mapbox.com/datasets/v1/" + MAPS_USER + "/" + DATASET_ID + "/features?access_token=" + MAPS_TOKEN
resp = requests.get(featurl)
print(resp.json())
print("\n")

# add features to a dataset
posturl = "https://api.mapbox.com/datasets/v1/" + MAPS_USER + "/" + DATASET_ID + "/features/" + feature_id + "?access_token=" + MAPS_TOKEN
resp = requests.post(posturl, data=body)
print(resp.json())



# add features to a datasets
