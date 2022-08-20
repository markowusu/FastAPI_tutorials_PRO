
#  We will be creating a database session 
#  I will also explain how to each import from sql_alchemy works and what we will use it for.
#  yielding the database session 

# orm
# objects --->  Relation ( Table)            # Table --> colum, row 
# user   --->   User ( User Table)                       name  age  nick_name                                                      
#  |                                                      kofi  8    Buju
#  |___ --> name , age , nick_name
#  class User():
#  eg. of a class -- instance in our code 

from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 
from pydotenv import load_env
import os 

#  create_engine -- will help bind the db connection using the db url 
#  sessionmaker which will help create a session class 
#  declarative_base: function-> return a class -- we will be using it to create a class that will us help map objects to relations the db 

#  create an engine --- connection to the database 
#  sessionmaker to create a session class that will be used in a db session dependency 
#  declarative_base function to  Base that maps our object to relations in the database 

load_env(".env")
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
dbSession = sessionmaker(bind=engine, autoflush= True, autocommit=False )
Base = declarative_base()


#  connect to the database 
#  create objects to be in the db
#  create routes  
#  crud  operations ... 
