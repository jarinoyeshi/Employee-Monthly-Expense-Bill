

# FOR FLASK,  SQLALCHEMY,  SESSIONMAKER
from flask import Flask,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

# FOR JSON SERIALIZATION
from marshmallow import Schema,fields

# FOR DATABASE CONNECTION
import urllib
import pyodbc
from sqlalchemy import create_engine

# FOR MODEL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,DateTime,Integer,String,Boolean,ForeignKey,Numeric,Function
from datetime import datetime


#  FOR BLUEPRINT
from flask import Blueprint, request



# Common fields for all models 
class BaseModel():
    IsActive = Column(Boolean,default=True)
    CreatedByID= Column(String,nullable=False)
    CreatedOn= Column(DateTime,default=datetime.now)
    UpdatedByID= Column(String)
    UpdatedOn = Column(DateTime,onupdate=datetime.now)
    
    
    def getAnObject(self, data: dict):
        for column in data:
            setattr(self,column,data[column])
        return self
            


Base= declarative_base()

#server information
server = "192.168.42.6"
username= "sa"
password = urllib.parse.quote_plus("e0LZ0G*#%B9)G9}P95")
database = "MonthlyExpenseBillJarin"
    
connectionString = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=Sql Server"
engine = create_engine(connectionString,echo=True, pool_recycle=3600, use_setinputsizes=False)



# Session Making 
Session= sessionmaker(bind=engine)
