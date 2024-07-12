
#---------------------------------------

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
import os

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret,
                       connect_args={"ssl": {
                           "ssl_ca": "isrgrootx1.pem"
                       }},
                       future=True)

metadata = MetaData()

jobs = Table(
    'jobs', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(250), nullable=False),
    Column('location', String(250), nullable=False),
    Column('salary', Integer),
    Column('currency', String(18)),
    Column('responsibilities', Text),  # Use Text for larger text fields
    Column('requirements', Text)
)

# Create tables in database if they do not exist
metadata.create_all(engine)
