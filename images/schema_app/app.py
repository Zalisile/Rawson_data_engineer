#!/usr/bin/env python
import time
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.util import deprecations
deprecations.SILENCE_UBER_WARNING = True

print("Waiting for 5 seconds.")
time.sleep(5)
print("Wait is over.")

# Connect to the database
msqldb_uri = 'mysql://codetest:swordfish@database:3306/codetest'
engine = sqlalchemy.create_engine(msqldb_uri)

# Execute schema.sql
with engine.connect() as con:
    with open('./schema.sql') as file:
        query = text(file.read())
        con.execute(query)

print("Waiting for 5 seconds.")
time.sleep(5)
print("Wait is over.")

# Fetch tables and print them
inspector = sqlalchemy.inspect(engine.connect())
table_names = inspector.get_table_names()
for table_name in table_names:
    print(table_name)