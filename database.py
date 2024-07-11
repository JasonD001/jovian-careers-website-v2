from sqlalchemy import create_engine, text

db_connection_string =  "mysql+pymysql://3fhxh8nve6iyVbK.root:SCVEFrEbCG135vaO@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "isrgrootx1.pem"
        }
    }
)


with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all()) 

