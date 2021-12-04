#MtG Historical Analysis Part 1.1: Fetching Data
#The dataset will be downloaded via the MtG API and saved locally as a JSON file.
import time, requests, json, re

#Relevant variables for the API requests
setsURL = 'https://api.magicthegathering.io/v1/sets'
cardsURL = 'https://api.magicthegathering.io/v1/cards'
nextPage = re.compile(r'(?<=<)\S*(?=>; rel="next")')
jsonOut = {"sets": [], "cards": []}

#Request data and write each set to the JSON file
incr = 1
while setsURL != None:
    r = requests.get(setsURL)
    data = r.json()
    for d in data.get('sets'):
        jsonOut["sets"].append(d)
        print('Added set #{}: {}.'.format(incr, d.get('name')))
        incr += 1
    setsURL = re.search(nextPage, r.headers.get('link'))
    if setsURL:
        setsURL = setsURL[0]
        print('\nMoving to next page. Ratelimit remaining: {}.\n'.format(r.headers.get('Ratelimit-Remaining')))
    else:
        setsURL = None
    time.sleep(3)
#
# #Request data and write cards to the file
incr = 1
while cardsURL!= None:
    r = requests.get(cardsURL)
    data = r.json()
    for d in data.get('cards'):
        jsonOut["cards"].append(d)
        print('Added card #{}: {}.'.format(incr, d.get('name')))
        incr += 1
    cardsURL = re.search(nextPage, r.headers.get('link'))
    if cardsURL:
        cardsURL = cardsURL[0]
        print('\nMoving to next page. Ratelimit remaining: {}.\n'.format(r.headers.get('Ratelimit-Remaining')))
    else:
        cardsURL = None
    time.sleep(3)

#Write to file
with open('mtg.json', 'w') as fileout:
    json.dump(jsonOut, fileout)

#Close the file
fileout.close()
