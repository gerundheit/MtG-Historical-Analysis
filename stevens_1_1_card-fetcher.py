#MtG Historical Analysis Part 1.1: Fetching Data
#The dataset will be downloaded via the MtG API and saved locally as a series of JSON files.
import os, time, requests, json

#Write card records to their own directory
if not os.path.exists('cards'):
    os.makedirs('cards')

#Relevant variables for the API requests
url = 'https://api.magicthegathering.io/v1/cards'
pageNum = 1

#Request data and write each card to its own individual JSON file
while pageNum < 650: #Built-in stop: each client is rate-limited to 1000 requests, but there are actually only about 640 pages of cards when you display the default/max 100 at a time
    r = requests.get(url+'?page={}'.format(pageNum))
    if r.headers['Ratelimit-Remaining'] == '1': #Extra stop in case we hit rate limit. The docs don't specify whether the 1000 requests is per day or some smaller unit of time.
        print('Ratelimit break reached: {}'.format(r.headers['Ratelimit-Remaining']))
        break
    data = r.json()
    for d in data['cards']: #Get data for each individual card
        print(d['name'])
        id = d['id']
        fileout = open('cards'+os.sep+str(id)+".json",'w') #Open the file for writing
        json.dump(d,fileout) #Use the json library to output the data
        fileout.close() #Close the file
    pageNum += 1
    print('\nMoving to page {}. Ratelimit remaining: {}.\n'.format(pageNum, r.headers['Ratelimit-Remaining']))
    time.sleep(3)
