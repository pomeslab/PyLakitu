from sqlalchemy import create_engine, DateTime, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

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
    replicas = relationship("Replica")

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

    sequences = relationship("Sequence")

    def __init__(self, reaction_coordinate):
        self.reaction_coordinate = reaction_coordinate
        self.start_time = datetime.now()


class Sequence(Base):
    '''
    This represents a row in our Seqeuence database
    '''

    __tablename__ = 'sequence'

    id = Column(Integer, primary_key=True)
    replica_id = Column(Integer, ForeignKey('replica.id'))

    sequence_number = Column(Integer)

    def __init__(self, sequence_number):
        self.sequence_number = sequence_number
