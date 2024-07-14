# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, DateTime
# import os
# from sqlalchemy.sql import text
# import datetime

# # Database connection string
# my_secret = os.environ['DB_CONNECTION_STRING']

# engine = create_engine(my_secret,
#                        connect_args={"ssl": {
#                            "ssl_ca": "isrgrootx1.pem"
#                        }},
#                        future=True)

# metadata = MetaData()

# # Jobs table definition
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

# # Applications table definition
# applications = Table(
#     'applications', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('job_id', Integer, nullable=False),
#     Column('fullname', String(100), nullable=False),
#     Column('email', String(100), nullable=False),
#     Column('linkedin', String(100), nullable=False),
#     Column('experience', Text, nullable=False),
#     Column('education', Text, nullable=False),
#     Column('work_experience', Text, nullable=False),
#     Column('created_at', DateTime, default=datetime.datetime.utcnow),
#     Column('updated_at', DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
# )

# # Function to add an application to the database
# def add_application_to_db(job_id, data):
#     with engine.connect() as conn:
#         query = text("""
#             INSERT INTO applications (job_id, fullname, email, linkedin, experience, education, work_experience, created_at, updated_at)
#             VALUES (:job_id, :fullname, :email, :linkedin, :experience, :education, :work_experience, :created_at, :updated_at)
#         """)

#         conn.execute(
#             query,
#             {
#                 'job_id': job_id,
#                 'fullname': data['fullname'],
#                 'email': data['email'],
#                 'linkedin': data['linkedin'],
#                 'experience': data['experience'],
#                 'education': data['education'],
#                 'work_experience': data['work_experience'],
#                 'created_at': datetime.datetime.utcnow(),
#                 'updated_at': datetime.datetime.utcnow()
#             }
#         )

# # Create tables in the database if they do not exist
# metadata.create_all(engine)

#-------------------------------------------------------------------------

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, DateTime
import os
from sqlalchemy.sql import text
import datetime

# Database connection string
my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret,
                       connect_args={"ssl": {
                           "ssl_ca": "isrgrootx1.pem"
                       }},
                       future=True)

metadata = MetaData()

# Jobs table definition
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

# Applications table definition
applications = Table(
    'applications', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('job_id', Integer, nullable=False),
    Column('fullname', String(100), nullable=False),
    Column('email', String(100), nullable=False),
    Column('linkedin', String(100), nullable=False),
    Column('experience', Text, nullable=False),
    Column('education', Text, nullable=False),
    Column('work_experience', Text, nullable=False),
    Column('created_at', DateTime, default=datetime.datetime.utcnow),
    Column('updated_at', DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
)

# Function to add an application to the database
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("""
            INSERT INTO applications (job_id, fullname, email, linkedin, experience, education, work_experience, created_at, updated_at)
            VALUES (:job_id, :fullname, :email, :linkedin, :experience, :education, :work_experience, :created_at, :updated_at)
        """)

        try:
            conn.execute(
                query,
                {
                    'job_id': job_id,
                    'fullname': data['fullname'],
                    'email': data['email'],
                    'linkedin': data['linkedin'],
                    'experience': data['experience'],
                    'education': data['education'],
                    'work_experience': data['work_experience'],
                    'created_at': datetime.datetime.utcnow(),
                    'updated_at': datetime.datetime.utcnow()
                }
            )
            conn.commit()  # Ensure the transaction is committed
            print("Application inserted successfully.")
        except Exception as e:
            print("Error inserting application:", str(e))

# Create tables in the database if they do not exist
metadata.create_all(engine)
