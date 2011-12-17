from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

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

    first_undefined_column = Column(String)
    second_undefined_column = Column(String

    def __init__(self, first_undefined_column, second_undefined_column):
        self.first_undefined_column = first_undefined_column
        self.second_undefined_column = second_undefined_column

