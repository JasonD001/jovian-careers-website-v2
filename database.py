# from sqlalchemy import create_engine

# db_connection_string = "mysql+pymysql://3fhxh8nve6iyVbK.root:SCVEFrEbCG135vaO@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?charset=utf8mb4"

# engine = create_engine(db_connection_string,
#                        connect_args={"ssl": {
#                            "ssl_ca": "isrgrootx1.pem"
#                        }})

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     # result_all = result.all()

#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(dict(row))

# print("type(result.all()): ", type(result_all))
# print('\n')
# print("result all()", result.all())
# print('\n')
# print("result.all() :", result_all)
# first_result = result_all[0]
# # print('\n')
# # print("result.all[0] : ", first_result)
# # print('\n')
# # print("type(first_result) : ", type(first_result))

# print('\n --------------------  Dictionary -------------------- ')
# # Convert the reuslt to a list of dictinaries
# first_result_dict = dict(result_all[0])
# print("type(first_result_dict : ", type(first_result_dict))
# print(first_result_dict)

# from sqlalchemy import create_engine, text

# from sqlalchemy import 
# from database import engine, jobs

# db_connection_string = "mysql+pymysql://3fhxh8nve6iyVbK.root:SCVEFrEbCG135vaO@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?charset=utf8mb4"

# engine = create_engine(
#     db_connection_string,
#     connect_args={
#         "ssl": {
#             "ssl_ca": "isrgrootx1.pem"
#         }
#     }
# )

# def row_to_dict(row):
#     return {key: value for key, value in row.items()}

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs"))
#     result_all = result.fetchall()

#     print("type(result): ", type(result))
#     print('\n')

#     print("type(result.all()): ", type(result_all))
#     print('\n')
#     print("result all()", result_all)
#     print('\n')

#     print('\n --------------------  Dictionary -------------------- ')
#     # Convert the result to a list of dictionaries
#     result_dicts = [row_to_dict(row) for row in result_all]
#     print("type(result_dicts): ", type(result_dicts))
#     print(result_dicts)


# database.py
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text

# # Define your database connection string and engine
# db_connection_string = "mysql+pymysql://3fhxh8nve6iyVbK.root:SCVEFrEbCG135vaO@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?charset=utf8mb4"
# engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "isrgrootx1.pem"}})

# metadata = MetaData()

# # Define your table structure (assuming 'jobs' table)
# jobs = Table(
#     'jobs', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('title', String(255)),
#     Column('location', String(255)),
#     Column('salary', Integer),
#     Column('currency', String(10)),
#     Column('description', Text),
#     Column('requirements', Text)
# )

# # Create tables in database if they do not exist
# metadata.create_all(engine)


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text

# Define your database connection string and engine with future mode
db_connection_string = "mysql+pymysql://3fhxh8nve6iyVbK.root:SCVEFrEbCG135vaO@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?charset=utf8mb4"
engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "isrgrootx1.pem"}}, future=True)

metadata = MetaData()

# Define your table structure (jobs table)
jobs = Table(
    'jobs', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    Column('title', String(250), nullable=False),
    Column('location', String(250), nullable=False),
    Column('salary', Integer),
    Column('currency', String(18)),
    Column('responsibilities', String(2000)),
    Column('requirements', String(2000))
)

# Create tables in database if they do not exist
metadata.create_all(engine)
