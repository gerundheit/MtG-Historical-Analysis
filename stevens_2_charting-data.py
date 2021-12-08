#MtG Historical Analysis Part 2: Charting Data
#MatPlotLib will be used to create charts of several historical trends of interest over the game's development.

#Import libraries
from datetime import datetime
import matplotlib.pyplot as plt, sqlite3 as s3, numpy as np, re

#Define function(s) and variables that will be used across multiple charts
pattern = re.compile(r'(?<=\')\w+(?=\')', re.IGNORECASE) #Allows us to extract individual card type strings from the list-like strings they come in
def dateCompare(dict): #Takes today's date and uses it to remove sets whose release dates are in the future from the data before charting
    todaysDate = datetime.now()
    popList = []
    for k in dict:
        releaseDate = chart1[k]['date']
        releaseDate = datetime.strptime(releaseDate, "%Y-%m-%d")
        if releaseDate > todaysDate:
            popList.append(k)
    for p in popList:
        dict.pop(p, 'Not found')

#Connect to the database
conn = s3.connect('stevens_1_2_database.db')
c = conn.cursor()

#Select data for chart 1: numbers of cards of each type printed per core set
chart1 = {}
c.execute("SELECT id, date FROM sets WHERE set_type = 'core' ORDER BY date ASC;")
table_data = c.fetchall()
for d in table_data: #Add set IDs, in order of publication, with dates of publication
    chart1.update({d[0]: {'date': d[1]}})
#Fetch set ID and types of each card
c.execute("SELECT set_id, types FROM cards;")
table_data = c.fetchall()
for d in table_data: #Add each card's type data to the counts inside the set dictionaries in chart1
    if d[0] in chart1.keys():
        types = re.findall(pattern, d[1])
        for type in types:
            if type in chart1[d[0]].keys():
                chart1[d[0]].update({type: chart1[d[0]][type] + 1})
            else:
                chart1[d[0]].update({type: 1})
dateCompare(chart1)

#Select data for chart 2: sample several card sets of interest and depict their mana curves for different card types, i.e. the number of cards in the set broken down by card type and mana cost
chart2 = {'LEA': {}, 'MH1': {}, 'AFR': {}}
cmcRange = [] #variable to store the range of available CMCs within the sample
c.execute("SELECT set_id, types, cmc FROM cards WHERE set_id = 'LEA' OR set_id = 'MH1' OR set_id = 'AFR';")
table_data = c.fetchall()
for d in table_data: #Add each card's type and CMC data to the counts inside the dictionaries in chart2
    setID, CMC = d[0], d[2]
    if CMC not in cmcRange:
        cmcRange.append(CMC)
    types = re.findall(pattern, d[1])
    for type in types:
        if type in chart2[setID].keys():
            if CMC in chart2[setID][type].keys():
                chart2[setID][type].update({CMC: chart2[setID][type][CMC] + 1})
            else:
                chart2[setID][type].update({CMC: 1})
        else:
            chart2[setID].update({type: {}})
cmcRange.sort()

#Select data for chart 3: show the power and toughness of creatures relative to their mana cost over time
# (power + toughness) / CMC

#Close the database
conn.close()

#Graph chart 1
sets, creatures, planeswalkers, instants, sorceries, enchantments, artifacts, lands = [], [], [], [], [], [], [], []
for k in chart1: #Populate the series
    sets.append(k)
    creatures.append(chart1[k].get('Creature', 0))
    planeswalkers.append(chart1[k].get('Planeswalker', 0))
    instants.append(chart1[k].get('Instant', 0))
    sorceries.append(chart1[k].get('Sorcery', 0))
    enchantments.append(chart1[k].get('Enchantment', 0))
    artifacts.append(chart1[k].get('Artifact', 0))
    lands.append(chart1[k].get('Land', 0))
plt.figure(num = 7)
x = np.arange(len(sets)) #set up marks for the x axis
plt.plot(x, creatures, color='#a50041')
plt.plot(x, planeswalkers, color='#8080ff')
plt.plot(x, instants, color='#ff8080')
plt.plot(x, sorceries, color='#264041')
plt.plot(x, enchantments, color='#a580c1')
plt.plot(x, artifacts, color='#004080')
plt.plot(x, lands, color='#804000')
plt.xticks(x, sets)
plt.title("Magic the Gathering: Printing Frequency of Major Card Types Per Core Set") #Label figure
plt.xlabel("MtG Core Sets")
plt.ylabel("Number of cards per type")
plt.legend(['Creatures', 'Planeswalkers', 'Instants', 'Sorceries', 'Enchantments', 'Artifacts', 'Lands'])
plt.show()

#Graph chart 2

#Graph chart 3
