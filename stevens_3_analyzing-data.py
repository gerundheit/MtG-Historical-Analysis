#MtG Historical Analysis Part 3: Analyzing Data
#This analysis will dig into the frequency with which Magic the Gathering has published cards of different type and cost over time, starting with the same data as the charts described in Part 2 and following any interesting trends which emerge in more detail. Additionally, the data set will be analyzed to select a few mechanical keywords and perform an analysis of how frequently those keywords appear in cards of each set, e.g.: the 2021 "Midnight Hunt" set is known for its use of cards with keyword "disturb": in what set and year did this keyword first appear, and how frequently has it been used since? Finally, create an HTML table showing how many counterspells were published in each set and what years those sets occurred in. Display all table data and charts in one HTMl filefor easier viewing.

#Import libraries
import sqlite3 as s3, pandas as pd, numpy as np, os

#Connect to the database
conn = s3.connect('stevens_1_2_database.db')
c = conn.cursor()

#Dig into Chart 3: find a better way to display the frequency of the quotients over time
df = pd.read_sql_query("SELECT set_id, cmc, power, toughness FROM creatures;", conn) #create a dataframe of all creature data
df = df[df.power != -1] #drop rows with power or toughness of -1
df = df[df.toughness != -1]
df.loc[df['cmc'] == 0, 'cmc'] = 0.01 #replace CMCs of 0 with 0.01 to avoid dividing by zero when we create the quotients; setting the CMC at 0.1 fudges the numbers a little but still gives creatures that are free to cast quotients that are distinct from and advantaged over creatures that cost 1 to cast
df = df.reset_index(drop=True) #reset the index for cleaner numbering
df['cmc_quotient'] = (df['power'] + df['toughness']) / df['cmc'] #calculate CMC quotient for each row
htmlFile = open('stevens_3_1_data-analysis.html', 'w') #open HTML file for output and write header and charts
htmlFile.write('''<!DOCTYPE html>
<html>
<style>table, th, td {
    border:1px solid black; border-collapse: collapse;
}
</style>
<body>
\n<h1>Magic the Gathering Historical Analysis: Results</h1>
<p>Analysis performed by Ray Stevens for Simmons University SLIS LIS487-OL1 with Dr. Catherine Dumas, December 2021.</p>
\n<h2>Chart 1: Printing Frequency</h2>
<img src="chart1.png" alt="Chart 1: Magic the Gathering: Printing Frequency of Major Card Types Per Core Set" style="width:90%;>"<br>
\n<h2>Charts 2-1 through 2-3: Mana Curve</h2>
<img src="chart2-1.png" alt="Chart 2-1: Mana Curve by Card Type: Adventures in the Forgotten Realms" style="width:80%;>"<br>
<img src="chart2-2.png" alt="Chart 2-2: Mana Curve by Card Type: Limited Edition Alpha" style="width:80%;>"<br>
<img src="chart2-3.png" alt="Chart 2-3: Mana Curve by Card Type: Modern Horizons 1" style="width:80%;>"<br>
\n<h2>Chart 3: Creatures</h2>
<img src="chart3.png" alt="Chart 3: MtG Creatures: Power/Toughness Compared to Converted Mana Cost Over the Years" style="width:70%;>"<br>
''')

#start first table
htmlFile.write('''\n<h2>CMC Quotient Data for Extent Magic the Gathering Creatures by Set</h2>
<p>"CMC" = "converted mana cost," the mana that must be paid to cast a spell card. Here, CMC quotient shows the relationship between a creature spell's stats and its CMC, where quotient = (power + toughness)/CMC. Creatures with variable or non-numerical power and toughness have been omitted from the set.</p>

<table style=\"width:100%\">
    <tr>
        <th>Set ID</th>
        <th>Publication Date</th>
        <th>n of Creatures</th>
        <th>Average CMC Quotient</th>
        <th>Median CMC Quotient</th>
        </tr>
\n''')
c.execute("SELECT id, name, date FROM sets ORDER BY date ASC;") #fetch all set publication dates
sets_data = c.fetchall()
for set in sets_data: #iterate through sets with pub dates
    n = sum(df['set_id'] == set[0]) #find the n of creatures in each set as represented in the dataframe
    mean = df.loc[df.set_id.shift() == set[0], 'cmc_quotient'].mean()
    median = df.loc[df.set_id.shift() == set[0], 'cmc_quotient'].median()
    if n != 0: #enter nonzero set stats into the table
        htmlFile.write('''
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        </tr>\n'''.format(set[0], set[2], n, round(mean, 2), round(median, 2)))
htmlFile.write('''</table>''') #conclude HTML table

#Make an HTML table depicting the most frequent keyword appearing in each set (pick five sets)
c.execute("SELECT set_id, card_text FROM cards ORDER BY set_id ASC;")
inn_data = c.fetchall()
c.execute("SELECT id, name, date FROM sets WHERE id = 'ISD' OR id = 'DKA' OR id = 'AVR' OR id = 'MID' OR id = 'VOW' ORDER BY date ASC;")
sets_data = c.fetchall()
keywords = ['deathtouch', 'defender', 'double strike', 'enchant', 'equip', 'first strike', 'flash', 'flying', 'haste', 'hexproof', 'indestructible', 'intimidate', 'forestwalk', 'plainswalk', 'islandwalk', 'swampwalk', 'mountainwalk', 'lifelink', 'protection', 'reach', 'shroud', 'trample', 'vigilance', 'ward', 'banding', 'rampage', 'cumulative upkeep', 'flanking', 'phase', 'buyback', 'shadow', 'cycling', 'cycle', 'echo', 'horsemanship', 'fading', 'kicker', 'flashback', 'madness', 'fear', 'morph', 'amplify', 'provoke', 'storm', 'affinity', 'entwine', 'modular', 'sunburst', 'bushido', 'soulshift', 'splice', 'offering', 'ninjutsu', 'epic', 'convoke', 'dredge', 'transmute', 'bloodthirst', 'haunt', 'replicate', 'forecast', 'graft', 'recover', 'ripple', 'split second', 'suspend', 'vanishing', 'absorb', 'aura swap', 'delve', 'fortify', 'frenzy', 'gravestorm', 'poisonous', 'transfigure', 'champion', 'changeling', 'evoke', 'hideaway', 'prowl', 'reinforce', 'conspire', 'persist', 'wither', 'retrace', 'devour', 'exalted', 'unearth', 'cascade', 'annihilator', 'level up', 'rebound', 'totem armor', 'infect', 'battle cry', 'living weapon', 'undying', 'miracle', 'soulbond', 'overload', 'scavenge', 'unleash', 'cipher', 'evolve', 'extort', 'fuse', 'bestow', 'tribute', 'dethrone', 'hidden agenda', 'outlast', 'prowess', 'dash', 'exploit', 'menace', 'renown', 'awaken', 'devoid', 'ingest', 'myriad', 'surge', 'skulk', 'emerge', 'escalate', 'melee', 'crew', 'fabricate', 'partner', 'undaunted', 'improvise', 'aftermath', 'embalm', 'eternalize', 'afflict', 'ascend', 'assist', 'jump-start', 'mentor', 'afterlife', 'riot', 'spectacle', 'escape', 'companion', 'mutate', 'encore', 'boast', 'foretell', 'demonstrate', 'daybound', 'disturb', 'decayed', 'cleave', 'training', 'investigate', 'blood token', 'transform']#this list was transcribed from https://mtg.fandom.com/wiki/Keyword_ability because the MtG API does not currently cover keyword abilities. I have added "blood token" and "transform" because while they are not technically on the rules' list of abilities, they are core mechanics of one or more of the Innistrad sets.
#start the new table
htmlFile.write('''\n<h2>Keyword Usage in the Innistrad Sets</h2>
<p>Five sets of cards have been published for the Innistrad setting in Magic the Gathering. This table shows the use of certain mechanical keywords in these sets.</p>
<table style=\"width:100%\">
    <tr>
        <th>Set</th>
        <th>Publication Date</th>
        <th>Keywords Used</th>
        <th>Most-Used Keyword</th>
        </tr>\n''')

hits = {}
for set in sets_data: #iterate through sets
    hits.update({set[0]: {}})
    for word in keywords:
        for card in inn_data: #search each card for each keyword and add relevant keywords into a dictionary
            if card[0] == set[0] and card[1] != None: #looks through each card that's actually in the set currently being considered
                if word in card[1].lower(): #adds to keyword counts where it finds them
                    hits[set[0]][word] = (hits[set[0]].get(word, 0) + 1)
    htmlFile.write('''
    <tr>
        <td>{} ({})</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>\n'''.format(set[1], set[0], set[2], ', '.join(hits[set[0]].keys()), max(hits[set[0]], key=lambda key: hits[set[0]][key]))) #write the keywords and winner to the other two columns
htmlFile.write('''</table>
</body>
</html>''') #close HTML table

#close files
htmlFile.close()
conn.close()
