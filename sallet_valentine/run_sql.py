import sqlalchemy
from sqlalchemy import *
from sqlalchemy.testing import db

db_url = 'postgresql://root:root@localhost:5432/store'
engine = create_engine(db_url)
connection = engine.connect()

#create
create_table = open("create_table.sql")
escaped_sql = sqlalchemy.text(create_table.read())
connection.execute(escaped_sql)




