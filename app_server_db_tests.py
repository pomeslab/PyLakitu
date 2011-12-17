import unittest
from app_server_db import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class JobDatabaseTestCase(unittest.TestCase):
    '''
    This tests the basic database functionality of the Job table
    '''

    def setUp(self):
        #Initialize an in memory database
        self.engine = create_engine('sqlite:///:memory:')
        #Create tables from metadata
        Base.metadata.create_all(self.engine)

    def test_commit(self):
        #This tests creating a Job table and commiting a row
        Session = sessionmaker(bind=self.engine)
        session_instance = Session()
        j1 = Job("localhost", "C:/windows/system32/")
        session_instance.add(j1)
        session_instance.close()


#j1.replicas=[Replica("poop1"), Replica("poop2")]

if __name__ == '__main__':
    unittest.main()
