#MtG Historical Analysis Part 0: Proof of Access
import requests, time, os, json

#make a folder for the files
if not os.path.exists("sets"):
    os.makedirs("sets")

#equest the first page of set data
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
