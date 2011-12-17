import unittest
from app_server_db import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SQLDatabaseTestCase(unittest.TestCase):
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

        #Fill in the relationship field to the replicas
        j1.replicas=[Replica("item 1","item 2"),Replica("poop 1","poop 2")]

        #Confirm that the session instance contains no Jobs/Replicas yet
        assert session_instance.query(Job).count() is 0
        assert session_instance.query(Replica).count() is 0

        session_instance.add(j1)

        #Confirm they are in the session now
        assert session_instance.query(Job).count() is 1
        assert session_instance.query(Replica).count() is 2

        session_instance.commit()
        session_instance.close()

        #Confirm they were committed to the DB with a new session
        new_session_instance = Session()
        assert new_session_instance.query(Job).count() is 1
        assert new_session_instance.query(Replica).count() is 2
        new_session_instance.close()

if __name__ == '__main__':
    unittest.main()
