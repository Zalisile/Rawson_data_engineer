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

cursor=db.cursor()

cursor.execute("SHOW TABLES")

for table_name in cursor:
   print(table_name)