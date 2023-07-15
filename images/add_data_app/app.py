#!/usr/bin/env python
import time
import csv
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.util import deprecations
deprecations.SILENCE_UBER_WARNING = True


# Delay for a few seconds before connecting to the database
print("Waiting for 80 seconds.")
time.sleep(80)
print("Wait is over.")


# Connect to the database
msqldb_uri = 'mysql://codetest:swordfish@database:3307/codetest'
engine = sqlalchemy.create_engine(msqldb_uri)

# Delay for a few seconds before connecting to the database
print("Waiting for 5 seconds.")
time.sleep(5)
print("Wait is over.")

metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the table
Peope_data = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)

# Read the CSV data file into the table
with open('./data/people.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    rows = []
    for row in reader:
        rows.append({'given_name': row[0], 'family_name': row[1], 'date_of_birth': row[2], 'place_of_birth': row[3] })
    # Delay for a few seconds before connecting to the database
    print("Waiting for 5 seconds.")
    time.sleep(5)
    print("Wait is over.")    

    # Insert multiple rows at once
    engine.connect().execute(Peope_data.insert().values(rows))
 
print("Waiting for 5 seconds.")
time.sleep(5)
print("Wait is over.")