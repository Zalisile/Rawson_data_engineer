#!/usr/bin/env python
import json
import time
import csv
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.util import deprecations
deprecations.SILENCE_UBER_WARNING = True


# Delay for a few seconds before connecting to the database
print("Waiting for 120 seconds.")
time.sleep(120)
print("Connection to the database established.")


# Connect to the database
msqldb_uri = 'mysql://codetest:swordfish@database/codetest'
engine = sqlalchemy.create_engine(msqldb_uri)

# Delay for a few seconds before connecting to the database
print("Waiting for 5 seconds.")
time.sleep(5)
print("Connection to the database established.")

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
    print("Waiting for 15 seconds.")
    time.sleep(15)
    print("Table creation done")    

    # Insert multiple rows at once
    engine.connect().execute(Peope_data.insert().values(rows))
 
print("Waiting for 240 seconds.")
time.sleep(240)
print("Data insertion done")


places_data = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)

# Read the CSV data file into the table
with open('./data/places.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    rows = []
    for row in reader:
        rows.append({'city': row[0], 'county': row[1], 'country': row[2] })
    # Delay for a few seconds before connecting to the database
    print("Waiting for 15 seconds.")
    time.sleep(15)
    print("Table creation done")    

    # Insert multiple rows at once
    engine.connect().execute(places_data.insert().values(rows))


print("Waiting for 120 seconds.")
time.sleep(180)
print("Data insertion done, SQL execution is in progress and creation of the json file")


# Execute the SQL query
query = """
SELECT places.country, COUNT(people.place_of_birth) AS birth_count
FROM people
INNER JOIN places ON places.city = people.place_of_birth
GROUP BY places.country
ORDER BY places.country DESC;
"""
result = engine.execute(text(query))

# Fetch all rows from the result
rows = result.fetchall()

# Prepare the output data
output_data = []
for row in rows:
    output_data.append({"country": row["country"], "birth_count": row["birth_count"]})

# Define the output file path
output_file = "./data/summary_output.json"

# Write the data to the JSON file
with open(output_file, "w") as json_file:
    json.dump(output_data, json_file, indent=4)

print(f"Summary output saved to {output_file}")
