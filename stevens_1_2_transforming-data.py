#MtG Historical Analysis Part 1.2: Transforming Data
#Data will be extracted from local JSON files and loaded into database files/tables as needed to perform the analysis described in Parts 2 & 3.

#Import libraries
import json, sqlite3 as s3

#Create the database
conn = s3.connect('stevens_1_2_database.db')
c = conn.cursor()

#Drop tables on re-run of program
c.execute('DROP TABLE IF EXISTS sets')
c.execute('DROP TABLE IF EXISTS creatures')
c.execute('DROP TABLE IF EXISTS cards')

#Create tables
sql_sets_table = """CREATE TABLE sets (
                                id text PRIMARY KEY,
                                name text NOT NULL,
                                set_type text,
                                date text
                            );"""
sql_creatures_table = """CREATE TABLE creatures (
                                id text PRIMARY KEY,
                                name text NOT NULL,
                                set_id text NOT NULL,
                                cmc real,
                                power integer,
                                toughness integer
                            );"""
sql_cards_table = """CREATE TABLE cards (
                                id text NOT NULL,
                                name text NOT NULL,
                                set_id text NOT NULL,
                                cmc real,
                                types text,
                                card_text text
                            );"""
c.execute(sql_sets_table)
c.execute(sql_creatures_table)
c.execute(sql_cards_table)

#Load JSON data into tables relevant to desired analysis
data = json.load(open('mtg.json'))
for d in data.get('sets'):
    c.execute("INSERT INTO sets VALUES (?,?,?,?)", (d.get('code'), d.get('name'), d.get('type'), d.get('releaseDate')))
for d in data.get('cards'):
    c.execute("INSERT INTO cards VALUES (?,?,?,?,?,?)", (d.get('id'), d.get('name'), d.get('set'), d.get('cmc'), str(d.get('types')), d.get('text')))
    if 'Creature' in str(d.get('types')):
        power, toughness = d.get('power'), d.get('toughness')
        try: #This allows us to store power and toughness as integers in the table, even though some creatures have scores that are not integers. Marking these with a -1 allows us to exclude them from tripping up statistical analysis later.
            power = int(power)
        except:
            power = -1
        try:
            toughness = int(toughness)
        except:
            toughness = -1
        c.execute("INSERT INTO creatures VALUES (?,?,?,?,?,?)", (d.get('id'), d.get('name'), d.get('set'), d.get('cmc'), power, toughness))

#Checks: print some selected data to terminal for checking
print('Test: sets Table Selection: 5 earliest sets sorted by date')
c.execute("SELECT * FROM sets ORDER BY date LIMIT 5;")
table_data = c.fetchall()
for d in table_data:
    print('Set ID: {}\nSet Name: {}\nSet Type: {}\nSet Date: {}\n\n'.format(d[0], d[1], d[2], d[3]))

print('Test: cards Table Selection: 10 cards with converted mana cost greater than or equal to 7')
c.execute("SELECT * FROM cards WHERE cmc >= 7 ORDER BY cmc DESC LIMIT 10;")
table_data = c.fetchall()
for d in table_data:
    print('Card: {}\nCMC: {}\nText: {}\n\n'.format(d[1], d[3], d[5]))

print('Test: creatures Table Selection: 10 creatures with 6 power')
c.execute("SELECT * FROM creatures WHERE power = 6 LIMIT 10;")
table_data = c.fetchall()
for d in table_data:
    print('Creature: {}\nPower: {}\nToughness: {}\nCMC: {}\n\n'.format(d[1], d[4], d[5], d[3]))

#Save and close file
conn.commit()
conn.close()
