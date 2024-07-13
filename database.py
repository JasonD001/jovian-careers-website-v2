
# #---------------------------------------

# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
# import os

# my_secret = os.environ['DB_CONNECTION_STRING']

# engine = create_engine(my_secret,
#                        connect_args={"ssl": {
#                            "ssl_ca": "isrgrootx1.pem"
#                        }},
#                        future=True)

# metadata = MetaData()

# jobs = Table(
#     'jobs', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('title', String(250), nullable=False),
#     Column('location', String(250), nullable=False),
#     Column('salary', Integer),
#     Column('currency', String(18)),
#     Column('responsibilities', Text),  # Use Text for larger text fields
#     Column('requirements', Text)
# )

# # Create tables in database if they do not exist
# metadata.create_all(engine)


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

applications = Table(
    'applications', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('job_id', Integer, nullable=False),
    Column('fullname', String(100), nullable=False),
    Column('email', String(100), nullable=False),
    Column('linkedin', String(100), nullable=False),
    Column('experience', Text, nullable=False),
    Column('education', Text, nullable=False),
    Column('work_experience', Text, nullable=False)
)

# Create tables in database if they do not exist
metadata.create_all(engine)
