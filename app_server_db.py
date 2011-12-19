from sqlalchemy import create_engine, DateTime, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import datetime

Base = declarative_base()

class Job(Base):
    '''
    This object represents a row in our Job database that will be tracked 
    by the server
    '''

    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)

    hostname = Column(String)
    work_directory = Column(String)

    #this is a one-to-many relationship one job to replicas
    #this should connect with the following class in the Replica table
    #job_id = Column(Integer, ForeignKey('job.id'))
    replicas = relationship("Replica", backref="job")

    pbs_id = Column(Integer)
    pbs_num_of_nodes = Column(Integer)

    def __init__(self, hostname, work_directory):
        self.hostname = hostname
        self.work_directory = work_directory 

class Replica(Base):
    '''
    This object represents a row in our Replica database
    '''

    __tablename__ = 'replica'

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey('job.id'))

    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(String)
    reaction_coordinate = Column(Float)

    def __init__(self, reaction_coordinate):
        self.reaction_coordinate = reaction_coordinate
        self.start_time = datetime.now()
