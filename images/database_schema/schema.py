import sqlalchemy
from sqlalchemy import text

# connect to the database
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

with connection as con:
    with open("schema.sql") as file:
        query = text(file.read())
        con.execute(query)

metadata = sqlalchemy.schema.MetaData(engine)