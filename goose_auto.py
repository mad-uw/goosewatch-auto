import urllib
import urllib2
import json
import time
import csv

#Get access token
token_url = 'https://www.arcgis.com/sharing/rest/oauth2/token/'
values = {'client_id': 't3E7JqOoSrsw8CBe',
          'client_secret':'3cd75e9716c5442199d783234ed5b78c',
          'grant_type':'client_credentials'}

data = urllib.urlencode(values)
req = urllib2.Request(token_url, data)
response = urllib2.urlopen(req)
response_data = response.read()
json_response = json.loads(response_data)
token = json_response['access_token']

#Fetch data from AGOL
#goose_url = 'http://services1.arcgis.com/DwLTn0u9VBSZvUPe/arcgis/rest/services/GooseWatch_2015_Submissions/FeatureServer/0/query?where=Status+%3D+1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&quantizationParameters=&f=pgeojson&token='
goose_url = 'http://services1.arcgis.com/DwLTn0u9VBSZvUPe/arcgis/rest/services/GooseWatch_2015_Submissions/FeatureServer/0/query'
values = {'token': token,
          'f':'pgeojson',
          'where':'Status = 1',
          'outFields': 'submitdate, description, objectid',
          'outSR': 4326
          }
data = urllib.urlencode(values)
req = urllib2.Request(goose_url,data)
response = urllib2.urlopen(req)
response_data = response.read()
json_response = json.loads(response_data)

with open('1151GooseWatch.csv','wb') as csvfile:
    #Write header row
    goose_writer = csv.writer(csvfile, delimiter=',')
    goose_writer.writerow(['id','location','latitude','longitude','updated'])
    #Loop through data to make csv
    for f in json_response['features']:
        coords = f['geometry']['coordinates']
        x = str(coords[0])
        y = str(coords[1])
        desc = f['properties']['description']
        oid = str(f['id'])
        date = f['properties']['submitdate']
        date_time = time.gmtime(date/1000)
        date_str = time.strftime('%Y-%m-%d %H:%M:%S',date_time)
        row = [oid,desc,y,x,date_str]
        goose_writer.writerow(row)
