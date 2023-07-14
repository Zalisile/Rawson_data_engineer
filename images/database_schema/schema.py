#!/usr/bin/env python

import sqlalchemy
from sqlalchemy import text

# connect to the database
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

with connection as con:
    with open("schema.sql") as file:
        query = text(file.read())
        con.execute(query)

# Fetch tables and print them
table_names = engine.table_names()
for table_name in table_names:
    print(table_name)