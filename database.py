from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text

# Define your database connection string and engine with future mode
# unable to store data scretly deployment failed again and again  my_secret = os.environ['DB_CONNECTION_STRING']

db_connection_string = "mysql+pymysql://3fhxh8nve6iyVbK.root:SCVEFrEbCG135vaO@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?charset=utf8mb4"
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "isrgrootx1.pem"
                       }},
                       future=True)

metadata = MetaData()

# Define your table structure (jobs table)
jobs = Table(
    'jobs', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True,
           nullable=False), Column('title', String(250), nullable=False),
    Column('location', String(250), nullable=False), Column('salary', Integer),
    Column('currency', String(18)), Column('responsibilities', String(2000)),
    Column('requirements', String(2000)))

# Create tables in database if they do not exist
metadata.create_all(engine)

# the ideal practise is to keep all  the database relatd stuff here form app.py
# but the code is running so don't touch it
