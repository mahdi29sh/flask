from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()
 
########################################################################

class cv(Base):
    __tablename__="cv"

    cvid = Column(Integer,primary_key=True)
    uid = Column(Integer)
    content = Column(String)
    title = Column(String)

    def __init__(self,cvid , uid , content , title):
        self.cvid = cvid
        self.uid = uid
        self.content = content
        self.title = title
# create tables
Base.metadata.create_all(engine)