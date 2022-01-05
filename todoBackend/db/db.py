from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import os
from sqlalchemy import text

# Get environment variables
MYSQL_HOST = os.getenv('MYSQL_HOST')
print(MYSQL_HOST)

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@"+MYSQL_HOST+"/todos"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = True)
# with engine.connect() as connection:
#     result = connection.execute(text("select * from todos"))
#     print(result)
#     for row in result:
#         print("id:", row['id'])
#         print("title:", row['title'])
#         print("title:", row['description'])

engine = create_engine(SQLALCHEMY_DATABASE_URL)

        
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()