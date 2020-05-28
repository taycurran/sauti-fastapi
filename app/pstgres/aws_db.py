print("Hello")
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

# Create Connection Engine
engine = create_engine(os.getenv("aws_db_url"))

# Define Class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# returns a class
Base = declarative_base()