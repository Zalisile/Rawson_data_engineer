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
msqldb_uri = 'mysql://codetest:swordfish@database/codetest'
engine = sqlalchemy.create_engine(msqldb_uri)

print("Waiting for 5 seconds.")
time.sleep(5)
print("Wait is over.")