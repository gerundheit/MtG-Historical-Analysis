#MtG Historical Analysis Part 1.2: Transforming Data
#Data will be extracted from local JSON files and loaded into database files/tables as needed to perform the analysis described in Parts 2 & 3.

#Import libraries
import json, matplotlib, sqlite3 as s3, os

#Save the current working directory as a variable so we can return to it
retval = os.getcwd()

#Create the database
conn = s3.connect('stevens_1_2_database.db')
c = conn.cursor()

#Drop tables on re-run of program
c.execute('DROP TABLE IF EXISTS sets')
c.execute('DROP TABLE IF EXISTS creatures')
c.execute('DROP TABLE IF EXISTS cards')

#Create tables
sql_sets_table = """ CREATE TABLE sets (
                                id text PRIMARY KEY,
                                name text NOT NULL,
                                date text
                            );"""
sql_creatures_table = """CREATE TABLE creatures (
                                id text PRIMARY KEY,
                                name text NOT NULL,
                                set_id text NOT NULL,
                                CMC real,
                                power text,
                                toughness text
                            );"""
sql_cards_table = """CREATE TABLE cards (
                                id text PRIMARY KEY,
                                name text NOT NULL,
                                set_id text NOT NULL,
                                CMC text,
                                types text,
                                card_text text
                            );"""
c.execute(sql_sets_table)
c.execute(sql_creatures_table)
c.execute(sql_cards_table)

#Load JSON data into tables relevant to desired transformations
#Move to the sets directory
os.chdir(os.path.join(retval, 'sets'))
#Insert sets table data
for root, dirs, files in os.walk('.', topdown = True):
   for name in files:
       data = json.load(open(name))
       c.execute("INSERT INTO sets VALUES (?,?,?)", (data['code'], data['name'], data['releaseDate']))
#Move to the cards directory
os.chdir(os.path.join(retval, 'cards'))
#Insert creatures and cards table data
for root, dirs, files in os.walk('.', topdown = True):
   for name in files:
       data = json.load(open(name))
       c.execute("INSERT INTO cards VALUES (?,?,?,?,?,?)", (data['id'], data['name'], data['set'], data['cmc'], str(data['types']), data['text']))
       if 'Creature' in str(data['types']):
           c.execute("INSERT INTO creatures VALUES (?,?,?,?,?,?)", (data['id'], data['name'], data['set'], data['cmc'], data['power'], data['toughness']))

#Checks: output some selected terminal data for correctness
c.execute("SELECT * FROM sets ORDER BY date;")
table_data = c.fetchall()
for d in table_data:
    print('Set ID: {}\nSet Name: {}\nSet Date: {}\n\n'.format(d[0], d[1], d[2]))

#Save and close file
conn.commit()
conn.close()
