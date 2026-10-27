from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

sessionMaker = sessionmaker()

db_url = "postgresql://neondb_owner:npg_HruJnkq2fN3S@ep-wild-rice-b5685rwj-pooler.c-7.us-east-2.aws.neon.tech/learnpythondb?sslmode=require&channel_binding=require"
# db_url = "postgresql://postgres:password@localhost:5432/learnpythondb" 
engine = create_engine(db_url)
session= sessionmaker(autocommit= False,autoflush=False, bind=engine)
