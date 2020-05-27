# To Connect to Labs DB
from dotenv import load_dotenv
import os
import psycopg2
load_dotenv()

conn = psycopg2.connect(dbname=os.getenv("aws_db_name"),
                        user=os.getenv("aws_db_user"),
                        password=os.getenv("aws_db_password"),
                        host=os.getenv("aws_db_host"),
                        port=os.getenv("aws_db_port"))

curs = conn.cursor()
curs.close()
conn.close()
print("Done")
# ----------------------------------------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create Connection Engine
engine = create_engine(os.getenv("aws_db_url"))

# Define Class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# returns a class
Base = declarative_base()