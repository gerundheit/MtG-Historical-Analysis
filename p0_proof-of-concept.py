#Part 0: proof of access to dataset
import requests, time, os, json

#first, make a folder for the files we want to download
if not os.path.exists("sets"):
    os.makedirs("sets")

#we will request the first page of people data, then use the "next" key to keep going
url = "https://api.magicthegathering.io/v1/sets"
print(url)
r = requests.get(url)
data = r.json()
for d in data['sets']:
    print(d['name'])
    id = d['code']
    #open the file for writing
    fileout = open("sets"+os.sep+str(id)+".json",'w')
    #use the json library to output the data
    json.dump(d,fileout)
    #close the file!
    fileout.close()
