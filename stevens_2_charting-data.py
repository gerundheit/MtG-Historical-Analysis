#MtG Historical Analysis Part 2: Charting Data
#MatPlotLib will be used to create charts of several historical trends of interest over the game's development. One will be a multi-line graph depicting the numbers of cards of each major type published in each successive card set, to show trends in the relative numbers of e.g. creature cards vs. sorcery cards over time. Another series of charts will sample several card sets of interest and depict their mana curves for different card types, i.e. the number of cards in the set broken down by card type and mana cost. A third will show the power and toughness of creatures relative to their mana cost over time.

#Import libraries
import matplotlib.pyplot as plt, sqlite3 as s3, re, datetime

#Define functions
def dateCompare(dict): #Takes today's date and uses it to remove sets whose release dates are in the future from the data before charting
    todaysDate = datetime.datetime.now()
    popList = []
    for k in dict:
        releaseDate = chart1[k]['date']
        releaseDate = datetime.datetime.strptime(releaseDate, "%Y-%m-%d")
        if releaseDate > todaysDate:
            popList.append(k)
    for p in popList:
        dict.pop(p, 'Not found')

#Connect to the database
conn = s3.connect('stevens_1_2_database.db')
c = conn.cursor()

#Select data for chart 1: numbers of cards of each type printed per set
chart1 = {}
pattern = re.compile(r'(?<=\')\w+(?=\')', re.IGNORECASE)
c.execute("SELECT id, date FROM sets ORDER BY date ASC;")
table_data = c.fetchall()
for d in table_data: #Add set IDs, in order of publication, with dates of publication
    chart1.update({d[0]: {'date': d[1]}})
#Fetch set ID and types of each card
c.execute("SELECT set_id, types FROM cards;")
table_data = c.fetchall()
for d in table_data: #Add each card's type data to the counts inside the set dictionaries in chart1
    types = re.findall(pattern, d[1])
    for t in types:
        if t in chart1[d[0]].keys():
            chart1[d[0]].update({t: chart1[d[0]][t] + 1})
        else:
            chart1[d[0]].update({t: 1})
dateCompare(chart1)

#Graph chart 1

#Select data for chart 2: sample several card sets of interest and depict their mana curves for different card types, i.e. the number of cards in the set broken down by card type and mana cost

#Graph chart 2

#Select data for chart 3: show the power and toughness of creatures relative to their mana cost over time

#Graph chart 3

#Close the database
conn.close()
